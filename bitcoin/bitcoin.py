import requests

While True:
try:
    bitcoin_amount = float(input("Amount of Bitcoin: "))
except ValueError:
    continue
except TypeError