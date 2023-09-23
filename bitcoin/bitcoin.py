import requests
import json
import sys

def main(rate):

        bitcoin_amount = float(2)
        print(bitcoin_amount)
        print(type(bitcoin_amount))

        try:
            if type(bitcoin_amount) == float:
                bitcoin_price = float(bitcoin_amount) * float(rate)
                print(f"${bitcoin_price:,.4f}")
        except TypeError:
             sys.exit(1)
        except requests.RequestException:
              sys.exit(1)
        else:
             pass



    # while True: #while what is True? argv[]!!!!!
    #     try:
    #     except ValueError:
    #         continue
    #     except TypeError:
    #         continue
    #     except requests.RequestException:
    #         continue
    #     else:
    #         break

    #print(type(bitcoin_amount))

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
    #print(print_json(bpi))

    rate = bpi["rate_float"]
    #print(f"rate type: {type(rate)}")
    return rate



rate = return_rate()
main(rate)