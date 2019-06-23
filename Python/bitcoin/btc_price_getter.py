import requests

class BtcPriceGetter:
    def __init__(self, period=''):
        self.url = ''
        self.response = ''
        self.json = ''
    
    def priceNow(self):
        btc_api_url_now = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
        self.response = requests.get(btc_api_url_now)
        self.json = self.response.json()
        return float(self.json[0]['price_usd'])