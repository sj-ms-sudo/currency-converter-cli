import requests
import argparse
import sys
def convert(url , cur2):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed : {e}")
        sys.exit(1)
    conv = response.json()['conversion_rates']
    cur1 = response.json()['base_code']
    print(f"Current Exchange Rate")
    print(f"1{cur1} = {conv[cur2]}{cur2}")
def convertamount(url,cur2,amount):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed : {e}")
        sys.exit(1)
    conv = response.json()['conversion_rates']
    cur1 = response.json()['base_code']
    print(f"Current Exchange Rate")
    print(f"{amount}{cur1} = {amount*(conv[cur2])}{cur2}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Currency converter")
    parser.add_argument("cur1", help="Base currency code (e.g., USD)")
    parser.add_argument("cur2", help="Target currency code (e.g., INR)")
    parser.add_argument("-a", "--amount", help="Amount to convert", type=float)
    args = parser.parse_args()
    url = "https://v6.exchangerate-api.com/v6/"
    api_key = <YOUR_API_KEY>
    url = f"{url}{api_key}/latest/{args.cur1}"
    if args.amount:
        convertamount(url,args.cur2,int(args.amount))
    else:
        convert(url,args.cur2)