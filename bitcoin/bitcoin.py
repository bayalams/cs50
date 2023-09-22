import requests
import sys

# while True:
#     try:
#         bitcoin_amount = float(input("Amount of Bitcoin: "))
#     except ValueError:
#         continue
#     except TypeError:
#         continue
#     except requests.RequestException:
#         continue

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response = r.json()
print(response, type(response))
print()


