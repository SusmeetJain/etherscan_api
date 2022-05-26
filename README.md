# etherscan_api
This repo helps you with consuming Etherscan APIs in python.
Currently we just have a script to get Eth balance for a given address. Follow the steps below to get up and running with it.
 - Clone this repo/ download the script
 - Go to etherscan.io and get an API key (free)
 - Add your API key to the variable `API_KEY` in the script
 - Install the requests library
```
pip install requests
```
 - Run the script from the command line with the address of the wallet you want the balance for. Like this.
```
python get_eth_balance.py 0x631046bc261e0b2e3db480b87d2b7033d9720c90
```
You should see the eth balance for the address displayed.
