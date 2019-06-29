import time
from btc_ob_api.btc_price_getter import BtcPriceGetter
from btc_ob_api.usd_to_pln import usdToPlnConverter

btc = BtcPriceGetter()
pln = usdToPlnConverter()
amount = 0.064

while True:
    value = amount * btc.priceNow()
    print(pln.convert(value))
    time.sleep(30)