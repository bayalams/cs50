import requests
import json

def print_json(d):
    return json.dumps(d, indent=2)

# while True:
#     try:
#         bitcoin_amount = float(input("Amount of Bitcoin: "))
#     except ValueError:
#         continue
#     except TypeError:
#         continue
#     except requests.RequestException:
#         continue

# HTTP GET request to URL "api.coindesk.com" for asset/path "v1/bpi/currentprice.json"
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# Response in "dict" format.
response = r.json()
print(print_json(response), type(response))

print()
bpi = response["bpi"]["USD"]
print(print_json(bpi))
print(bpi["rate_float"])


