import requests
import time
from btc_price_getter import BtcPriceGetter

btc_api_url_day = 'https://apiv2.bitcoinaverage.com/indices/global/history/BTCUSD?period=daily&format=json'
btc_api_url_month = 'https://apiv2.bitcoinaverage.com/indices/global/history/BTCUSD?period=monthly&format=json'
btc_api_url_alltime = 'https://apiv2.bitcoinaverage.com/indices/global/history/BTCUSD?period=alltime&format=json'

tmp = BtcPriceGetter()

print(tmp.priceNow())