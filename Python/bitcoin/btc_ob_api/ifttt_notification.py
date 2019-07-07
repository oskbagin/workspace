import requests
import sys
from btc_ob_api.get_api_ob_entries import getApiObEntries, API_OB_TOKEN_NOT_IN_FILE

class iftttNotification:
    def __init__(self):
        keyToken = 'iftttKey'

        self.fetch = getApiObEntries()
        self.btcThresholdLow = self.fetch.getEntryFloat('btcLowThresholdPLN')
        self.btcThresholdHigh = self.fetch.getEntryFloat('btcHighThresholdPLN')

        # Check for errors.
        if self.fetch.isErrorState():
            print('The thresholds values are not present in the config file. Notification disabled.')
        else:
            # retrieve the keyToken value from the config file
            iftttKey = self.fetch.getEntry(keyToken)

            if iftttKey == API_OB_TOKEN_NOT_IN_FILE:
                print('Fatal: could not retrieve IFTTT applet key. Sending error notification and aborting...')
                # TODO Send failed init notification
                sys.exit(2)
            else:
                self.postUrl = 'https://maker.ifttt.com/trigger/btc-price/with/key/' + iftttKey

    def btcPriceNotify(self, btcPlnPrice):
        if btcPlnPrice < self.btcThresholdLow:
            requests.post(self.postUrl)

        if btcPlnPrice > self.btcThresholdHigh:
            requests.post(self.postUrl)
