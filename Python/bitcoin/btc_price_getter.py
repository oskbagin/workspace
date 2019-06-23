import requests

class BtcPriceGetter:
    def __init__(self, period=''):
        self.urlNow   = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
        self.urlToday = 'https://apiv2.bitcoinaverage.com/indices/global/history/BTCUSD?period=daily&format=json'
        self.urlMonth = 'https://apiv2.bitcoinaverage.com/indices/global/history/BTCUSD?period=monthly&format=json'
        self.urlAlltime = 'https://apiv2.bitcoinaverage.com/indices/global/history/BTCUSD?period=alltime&format=json'
        self.url = ''
        self.response = ''
        self.json = ''
    
    def btcGet(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()

    def priceNow(self):
        self.url = self.urlNow
        self.btcGet()        
        return float(self.json[0]['price_usd'])
    
    def pricesToday(self):
        self.url = self.urlToday
        self.btcGet()
        return self.json

    def priceTodayAverage(self):
        self.pricesToday()

        average = 0
        for row in self.json:
            if average == 0:
                average = row['average']
            else:
                average += row['average']
                average /= 2

        return average

