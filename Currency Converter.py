#Currency Converter

currencies = [
    "United States Dollar (USD)",
    "Euro (EUR)",
    "British Pound (GBP)",
    "Japanese Yen (JPY)",
    "Australian Dollar (AUD)",
    "Canadian Dollar (CAD)",
    "Swiss Franc (CHF)",
    "Chinese Yuan (CNY)",
    "New Zealand Dollar (NZD)",
    "Swedish Krona (SEK)",
    "Indian Rupee (INR)",
    "Brazilian Real (BRL)",
    "Russian Ruble (RUB)",
    "South Korean Won (KRW)",
    "South African Rand (ZAR)"
]

CurrencyDict = {
    "USD": 74.50,
    "EUR": 88.20,
    "GBP": 103.40,
    "JPY": 0.68,
    "AUD": 54.20,
    "CAD": 59.80,
    "CHF": 81.10,
    "CNY": 11.50,
    "NZD": 50.80,
    "SEK": 8.70,
    "INR": 1.00,
    "BRL": 13.80,
    "RUB": 1.00,
    "KRW": 0.065,
    "ZAR": 5.20
}

def CurrencyConverter():
    print("Welcome to the Currency Converter!")
    print("Here are the available currencies:")
    for currency in currencies:
        print(currency)
    currencyFrom = input("Please enter the currency you would like to convert from:")
    currencyTo = input("Please enter the currency you would like to convert to:")
    amount = float(input("Please enter the amount you would like to convert:"))
    convertedAmount = amount * (CurrencyDict[currencyTo] / CurrencyDict[currencyFrom])
    print(f"{amount} {currencyFrom} is equal to {convertedAmount} {currencyTo}")

CurrencyConverter()