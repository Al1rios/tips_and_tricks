
from forex_python.converter import CurrencyRates

converter = CurrencyRates()

def currency_converter():
    amount = int(input("Please enter amount to converter: "))

    from_currency = input("Enter the currency code of" \
                           " amount you are converting: ").upper()
    
    to_currency = input("Enter the currency code you" \
                        " are converting to:  ").upper()
    
    converter_amount = converter.convert(from_currency, to_currency, amount)

    return f'the amount is {converter_amount:.2f} and' \
        'the currency is {to_currency}'


print(currency_converter())