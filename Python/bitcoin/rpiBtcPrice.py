from btc_ob_api.btc_price_getter import BtcPriceGetter

btc = BtcPriceGetter()

price = btc.priceNow()

# replace with setting lcd
print(str(price) + ' USD')