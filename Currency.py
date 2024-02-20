from forex_python.converter import CurrencyRates
amount = float(input("Enter the amount of money: "))
from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., INR): ").upper()
c = CurrencyRates()
exchange_rate = c.get_rate(from_currency, to_currency)
converted_amount = amount * exchange_rate
if exchange_rate == 0:
    print("Invalid currency input. Please check your currencies and try again.")
else:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
