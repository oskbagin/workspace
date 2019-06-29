import time
from btc_price_getter import BtcPriceGetter
from usd_to_pln import usdToPlnConverter

btc = BtcPriceGetter()
pln = usdToPlnConverter()
amount = 0.064

while True:
    value = amount * btc.priceNow()
    print(pln.convert(value))
    time.sleep(30)