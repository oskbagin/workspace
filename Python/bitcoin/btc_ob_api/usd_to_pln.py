import requests
import sys
from btc_ob_api.get_api_ob_entries import getApiObEntries, API_OB_TOKEN_NOT_IN_FILE

class usdToPlnConverter:
    def __init__(self):
        currencyApiUrl = ''
        keyToken = 'currencyApi'
        usdBase = '?base=USD'

        currencyApiUrl = getApiObEntries().getEntry(keyToken)
        
        if currencyApiUrl == API_OB_TOKEN_NOT_IN_FILE:
            print('Fatal: USD-PLN API URL not set in the config file. Aborting...')
            sys.exit(1)
        else:
            self.usdUrl = currencyApiUrl + usdBase
            self.json = requests.get(self.usdUrl).json()
            self.usdToPln = float(self.json['rates']['PLN'])

    def convert(self, amount):
        return self.usdToPln * amount
