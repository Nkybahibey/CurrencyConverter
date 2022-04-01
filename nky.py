from forex_python.converter import CurrencyRates
import datetime as dt

date = dt.datetime(2021,12,3)

c = CurrencyRates()

print(c.get_rate('USD','EUR', date))
 
countries = ['EUR', 'INR','NGN','SEK','AUD']

for i in countries:
    print(c.get_rate('USD', i, date),i)
