import sys

from requests import get

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.etherscan.io/api"
ETHER_VALUE = 10 ** 18

def make_api_url(module, action, **kwargs):
	url = BASE_URL + f"?module={module}&action={action}&apikey={API_KEY}"

	for key, value in kwargs.items():
		url += f"&{key}={value}"

	return url

def get_account_balance(address):
	balance_url = make_api_url("account", "balance", address=address, tag="latest")
	response = get(balance_url)
	data = response.json()

	value = int(data["result"]) / ETHER_VALUE
	return value

if __name__ == "__main__":
    print ("Your account balance is : ", get_account_balance(sys.argv[1]))
