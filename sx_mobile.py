import requests
import random
from typing import Tuple
import currency_exchange

user = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
]

header = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
    "alt-used": "stockx.com",
    "appos": "web",
    "appversion": "0.1",
    "authorization": "",
    "connection": "keep-alive",
    "host": "stockx.com",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "te": "trailers",
    "user-agent": random.choice(user),
    "x-requested-with": "XMLHttpRequest",
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


def user_data(level: str, currency: str, account: str) -> None:
    """setting user selections"""
    global level_set, currency_set, account_set, rate, url_currency, fee
    level_set = level
    currency_set = currency
    account_set = account

    match currency_set:
        case 'gbp':
            url_currency = 'GBP'
            rate = currency_exchange.gbp()
        case 'usd':
            url_currency = 'USD'
            rate = currency_exchange.usd()
        case 'eur':
            url_currency = 'EUR'
            rate = currency_exchange.euro()

    match level_set:
        case '1':
            fee = float('0.87')
        case '2':
            fee = float('0.875')
        case '3':
            fee = float('0.88')
        case '4':
            fee = float('0.885')
        case '5':
            fee = float('0.89')



def get_data(sku: str) -> Tuple[str, str, str]:
    """fetch some data from the first endpoint to use them in second one."""
    req = requests.get(f"https://stockx.com/api/browse?&_search={sku}&dataType=product",
                       proxies={'https': random.choice(proxy_list), 'http': random.choice(proxy_list)}, timeout=5, headers=header)

    if req.status_code != 200:
        print(f"An error occurred while sending requests, Status code: {req.status_code}")

    data: dict = req.json()
    if data is None:
        print(f"An error occurred while returning json object, Product is None")

    try:
        section: str = data["Products"][0]
        name: str = section["name"]
        additional_desc: str = section["shoe"]
        url_key: str = section["urlKey"]
        url_image: str = section["media"]["smallImageUrl"]
    except Exception as e:
        print(f"An exception occurred while fetching data from first endpoint, Exception: {e}")

    return url_key, url_image, name, additional_desc


def fetch_data(key) -> str:
    """getting all the information from the second endpoint and modifying it to send to the embed"""
    req = requests.get(f"https://stockx.com/api/products/{key}?includes=market,360&currency={url_currency}&country=PL",
                       proxies={'https': random.choice(proxy_list), 'http': random.choice(proxy_list)}, timeout=5,
                       headers=header)

    if req.status_code != 200:
        print(f"An error occurred while sending requests, Status code: {req.status_code}")

    data: dict = req.json()
    if data is None:
        print(f"An error occurred while returning json object, Product is None")

    sizes_list: list[str, int] = []
    lowest_ask_list: list[int] = []
    highest_bid_list: list[int] = []
    payout_list: list[str] = []

    start_section: dict = data["Product"]["children"]
    for i in start_section.values():
        try:
            sizes_list.append(i["shoeSize"])
            lowest_ask_list.append(i["market"]["lowestAsk"])
            highest_bid_list.append(i["market"]["highestBid"])
        except Exception as e:
            print(f"An exception occurred while fetching data from second endpoint, Exception: {e}")

    for indeks, value in enumerate(lowest_ask_list):
        if value != 0:
            continue
        else:
            lowest_ask_list[indeks] = f"{[highest_bid_list[indeks]]}"

    kurs: float = rate

    for index, value in enumerate(lowest_ask_list):
        if type(value) == int:
            value = int(value * 0.95 - 1)  # new lowestask pattern
            value = value * fee - 4.33  # payout in selected currency, wpisz fee!
            value = value * kurs  # final payout in pln, wpisz tutaj dunkcje na kurs
            payout_list.append(f"{value:.2f}")
        else:
            value = float(value[1:-1])
            if value != 0:
                value = value * fee - 4.33
                value = value * kurs
                payout_list.append(f"({value:.2f})")
            else:
                payout_list.append(f"{value:.2f}")

    payout_string: str = "```\n"
    for a, b in zip(sizes_list, payout_list):
        payout_string += f"[{a}] {b}\n"

    return payout_string
