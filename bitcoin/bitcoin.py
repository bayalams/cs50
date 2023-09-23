import requests
import json

def main(rate):

    while True: #while what is True? Missing argv, correct input format
        try:
            bitcoin_amount = float(input("Amount of Bitcoin: "))
        except ValueError:
            continue
        except TypeError:
            continue
        except requests.RequestException:
            continue


    print(type(bitcoin_amount))
    bitcoin_price = float(bitcoin_amount) * float(rate)
    print(f"${bitcoin_price:,.4f}")

def print_json(d):
    return json.dumps(d, indent=2)


def return_rate():

    # HTTP GET request to URL "api.coindesk.com" for asset/path "v1/bpi/currentprice.json"
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Response in "dict" format.
    response = r.json()
    # print(print_json(response), type(response))
    # print()

    # Get "bpi" -> "USD" -> "rate_float" from response
    bpi = response["bpi"]["USD"]
    # print(print_json(bpi))

    rate = bpi["rate_float"]
    print(f"rate type: {type(rate)}")
    return rate



rate = return_rate()
main(rate)