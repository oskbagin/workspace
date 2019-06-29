import requests
import sys

class iftttNotification:
    def __init__(self):
        # TODO create class to get the tokens from api.ob file
        iftttKey = ''
        token = 'iftttKey:='
        with open('../../../api.ob') as file:
            fileContent = file.readlines()
            for line in fileContent:
                if token in line:
                    iftttKey = line[len(token):-1]
                    break
        if iftttKey == '':
            print('Could not retrieve IFTTT applet key.')
            # TODO Send failed init notification
            sys.exit(1)
        else:
            self.postUrl = 'https://maker.ifttt.com/trigger/btc-price/with/key/' + iftttKey
    
    def iftttBtcPriceNotify(self):
        requests.post(self.postUrl)
