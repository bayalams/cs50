import requests
import sys

while True:
    try:
        bitcoin_amount = float(input("Amount of Bitcoin: "))
    except ValueError:
        continue
    except TypeError:
        continue
    except requests.RequestException:
        continue
