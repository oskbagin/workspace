import time
# TODO workout the namings convention
from btc_ob_api.btc_price_getter import BtcPriceGetter as btcPrice
from btc_ob_api.ifttt_notification import iftttNotification as notify

btc = btcPrice()
ifttt = notify()

while True:
    plnValue = btc.getPlnPrice()
    print(plnValue)

    ifttt.btcPriceNotify(plnValue)
    # split into 3 threads, one for resetting notification timer, 
    # one for main print and one for storing in the db
    time.sleep(30)