import requests
import random
from typing import Tuple
import currency_exchange

user = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
]

header = {
        "User-Agent": random.choice(user),
        "authority": "sneakit.com",
        "accept": "application/json",
        "dnt": "1",
        "referer": "https://sneakit.com/listing/new"
}

proxy_list: list[str] = []


def proxy_format() -> None:
    """#changing the proxy format to use for requests"""
    if not proxy_list:
        with open("proxy.txt", "r") as file:
            for octet in file:
                octet = octet.strip().split(":")
                octet = f"http://{octet[2]}:{octet[3]}@{octet[0]}:{octet[1]}"
                proxy_list.append(octet)
    else:
        pass


def get_id(sku: str) -> Tuple[str, str, str]:
    """fetch some data from the first endpoint to use them in second one."""
    req = requests.get(f"https://sneakit.com/search/products/{sku}",
                       proxies={'https': random.choice(proxy_list), 'http': random.choice(proxy_list)}, timeout=5,
                       headers=header)

    if req.status_code != 200:
        print(f"An error occurred while sending requests, Status code: {req.status_code}")

    data: dict = req.json()
    if data is None:
        print(f"An error occurred while returning json object, Product is None")

    try:
        start_section: str = data["data"][0]
        sneakit_id: str = start_section["id"]
        name: str = start_section["name"]
        thumbnail_url: str = start_section["productable"]["presentation_img"].split()[2].replace('srcset="', '')
    except Exception as e:
        print(f"An exception occurred while fetching data from first endpoint, Exception: {e}")

    return sneakit_id, name, thumbnail_url


def fetch_payout(sneakit_id: str):

    req = requests.get(f"https://sneakit.com/search/product/{sneakit_id}", headers=header,
                       proxies={'https': random.choice(proxy_list), 'http': random.choice(proxy_list)}, timeout=5)

    if req.status_code != 200:
        print(f"An error occurred while sending requests, Status code: {req.status_code}")

    data: dict = req.json()
    if data is None:
        print(f"An error occurred while returning json object, Product is None")

    sizes_list: list[str, int] = []
    lowest_ask_list: list[int] = []

    for i in data["sizesPrices"]:
        sizes_list.append(i["size"])
        lowest_ask_list.append(i["price"])

    kurs: float = currency_exchange.euro()

    payout_list: list[str] = []
    for i in lowest_ask_list:
        if i:
            i = float(i)
            i -= 1
            i *= kurs
            payout_list.append(f"{i:.2f}")
        else:
            payout_list.append(f"{i}")

    final_str = '```\n'
    for a, b in zip(sizes_list, payout_list):
        final_str += f"[{a}] {b}\n"

    return final_str

