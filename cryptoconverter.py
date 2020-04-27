from datetime import datetime
import json
from urllib.request import urlopen

with urlopen('https://api.bittrex.com/api/v1.1/public/getmarketsummaries') as response:
    srccrypto = response.read()

data = json.loads(srccrypto)
data2 = json.dumps(data, indent=2)

with urlopen('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC') as response:
    bit = response.read()

price = json.loads(bit)
btc_usd = price['result']['Ask']

with urlopen('https://api.exchangeratesapi.io/latest') as response:
    srcexchange = response.read()

currency = json.loads(srcexchange)



coinsbtc = dict()
coinsusd = dict()
for x in data['result']:
    if x['MarketName'][:3]=='BTC':
        name = x['MarketName'][4:]
        price = x['Ask']
        coinsbtc[name] = price
    elif x['MarketName'][:3]=='USD':
        name = x['MarketName'][4:]
        price = x['Ask']
        coinsusd[name] = price
    else:
        continue



market = input('In what market do you want to buy? (USD or BTC) ').upper()
curren = input('Convert to what currency? ').upper()  
while True:
    if market == 'BTC':
        try:
            coin = input('What coin do you want to buy? ').upper()
            try:
                amount = float(input('How many coins do you want to buy? '))
            except:
                print('Invalid Input')
            usd_cur = currency['rates'][curren]/currency['rates']['USD']
            price = amount*coinsbtc[coin]*btc_usd*usd_cur
            print('The total price is', str(curren), str(price))
        except KeyError:
            print('The coin is not in the Bittrex Bitcoin market')
    elif market == 'USD':
        try:
            coin = input('What coin do you want to buy? ').upper()
            try:
                amount = float(input('How many coins do you want to buy? '))
            except:
                print('Invalid Input')
            usd_cur = currency['rates'][curren]/currency['rates']['USD']
            price = amount*coinsusd[coin]*usd_cur
            print('The total price is', str(curren), str(price))
        except KeyError:
            print('The coin is not in the Bittrex US Dollar market')
    reset = input().lower()
    if reset == 'reset':
        market = input('In what market do you want to buy? (USD or BTC) ').upper()
        curren = input('Convert to what currency? ').upper()  
    elif reset == 'quit':
        break    
    else:
        continue
