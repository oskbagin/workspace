import requests
import sys
sys.path.append('..')
from btc_ob_api.get_api_ob_entries import getApiObEntries, API_OB_TOKEN_NOT_IN_FILE

class iftttNotification:
    def __init__(self):
        keyToken = 'iftttKey'

        # retrieve the keyToken value from the config file
        iftttKey = getApiObEntries().getEntry(keyToken)

        if iftttKey == API_OB_TOKEN_NOT_IN_FILE:
            print('Could not retrieve IFTTT applet key. Sending error notification and aborting...')
            # TODO Send failed init notification
            sys.exit(2)
        else:
            self.postUrl = 'https://maker.ifttt.com/trigger/btc-price/with/key/' + iftttKey
    
    def iftttBtcPriceNotify(self):
        requests.post(self.postUrl)

tmp = iftttNotification()