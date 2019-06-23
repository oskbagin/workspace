import time
from btc_price_getter import BtcPriceGetter
from usd_to_pln import usdToPlnConverter

btc = BtcPriceGetter()

print("""
    BTC-USD Prizes:\n
    Now:                Press 1
    Today's average:    Press 2
    Convert to USD/PLN: Press 3
    Quit:               Press q
""")

choice = ''
while choice.lower() != 'q':
    choice = input()
    
    if choice == '1':
        print(str(btc.priceNow()) + ' USD')
    elif choice == '2':
        print(str(btc.priceTodayAverage()) + ' USD')
    elif choice == '3':
        print('Enter amount: ', end='')
        amount = float(input())
        value = amount * btc.priceNow()
        print('It is ' + str(value) + ' USD')
        pln = usdToPlnConverter()

        print('Converts to ' + str(pln.convert(value)) + ' PLN')
    else:
        pass