import requests
import json

def print_json(d):
    return json.dumps(d)

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
print(print_json(response), type(response))
print()
bpi = response["bpi"]["USD"]
print(bpi["rate_float"])


