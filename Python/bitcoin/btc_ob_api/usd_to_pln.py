import requests
import sys

class usdToPlnConverter:
    def __init__(self):
        currencyApiUrl = ''
        token = 'currencyApi:='
        usdToken = '?base=USD'

        with open('../../../api.ob') as file:
            fileContent = file.readlines()
            for line in fileContent:
                if token in line:
                    currencyApiUrl = line[len(token):-1]
                    break
        if currencyApiUrl == '':
            print('Something went wrong with the API while converting USD to PLN. Aborting...')
            sys.exit(1)
        else:
            self.usdUrl = currencyApiUrl + usdToken
            self.json = requests.get(self.usdUrl).json()
            self.usdToPln = float(self.json['rates']['PLN'])

    def convert(self, amount):
        return self.usdToPln * amount
