from btc_price_getter import BtcPriceGetter

btc = BtcPriceGetter()

price = btc.priceNow()

# replace with setting lcd
print(str(price) + ' USD')