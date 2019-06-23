import requests
import time
from btc_price_getter import BtcPriceGetter

tmp = BtcPriceGetter()
print(tmp.priceNow())
average = tmp.priceTodayAverage()
print(average)

