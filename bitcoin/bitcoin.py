import requests
import json
import sys

def main():

    if len(sys.argv) != 2:
        print("Missing command-line")
        sys.exit(1)

    rate = return_rate()
    bitcoin_amount = sys.argv[1] #tem de vir depois da verificação


    try:
        bitcoin_price = float(bitcoin_amount) * float(rate)
        print(f"${bitcoin_price:,.4f}")
    except ValueError:
            print("Command-line is not a number")
            sys.exit(1)
    except requests.RequestException:
            sys.exit(1)


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



if __name__ == "__main__":
    main()