import requests


def get_price_EURUSD():
    url = 'https://www.freeforexapi.com/api/live?pairs=EURUSD'

    try:
        response = requests.get(url)
        date = response.json()
        rate = date['rates']['EURUSD']['rate']
        return rate

    except requests.exceptions.RequestException as e:
        print('Error')


print(f"EUR/USD: {get_price_EURUSD()}")
