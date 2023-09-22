import requests

while True:
    try:
        bitcoin_amount = float(input("Amount of Bitcoin: "))
    except ValueError:
        continue
    except TypeError:
        continue