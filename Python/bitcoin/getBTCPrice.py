import requests
import time

btc_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

i = 0
while i < 10:
    response = requests.get(btc_api_url)
    response_json = response.json()

    print(response_json[0]['price_usd'])
    time.sleep(2)