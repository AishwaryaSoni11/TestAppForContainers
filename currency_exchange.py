import requests
import random


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


def euro() -> float:
    proxy_format()
    req = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=PLN&apikey=G94W6RQWNE5J9U73',
                       proxies={'https': random.choice(proxy_list), 'http': random.choice(proxy_list)}, timeout=5)

    if req.status_code != 200:
        print(f"An error occurred while getting currency rate, Status code: {req.status_code}")

    data: dict = req.json()
    if data is None:
        print(f"An error occurred while returning json object, Product is None")

    try:
        rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        rate = round(rate, 4)
    except Exception as e:
        print(f"An exception occurred while fetching data from first endpoint, Exception: {e}")

    return rate


def gbp() -> float:
    proxy_format()
    req = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GBP&to_currency=PLN&apikey=G94W6RQWNE5J9U73',
                       proxies={'https': random.choice(proxy_list), 'http': random.choice(proxy_list)}, timeout=5)

    if req.status_code != 200:
        print(f"An error occurred while getting currency rate, Status code: {req.status_code}")

    data: dict = req.json()
    if data is None:
        print(f"An error occurred while returning json object, Product is None")

    try:
        rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        rate = round(rate, 4)
    except Exception as e:
        print(f"An exception occurred while fetching data from first endpoint, Exception: {e}")

    return rate


def usd() -> float:
    proxy_format()
    req = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=PLN&apikey=G94W6RQWNE5J9U73',
                       proxies={'https': random.choice(proxy_list), 'http': random.choice(proxy_list)}, timeout=5)

    if req.status_code != 200:
        print(f"An error occurred while getting currency rate, Status code: {req.status_code}")

    data: dict = req.json()
    if data is None:
        print(f"An error occurred while returning json object, Product is None")

    try:
        rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        rate = round(rate, 4)
    except Exception as e:
        print(f"An exception occurred while fetching data from first endpoint, Exception: {e}")

    return rate
