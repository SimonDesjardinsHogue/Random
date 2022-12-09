import requests
import json

# Set the TradingView API URL
tv_url = 'https://api.tradingview.com/paper_trading/'

# Set the TradingView API key
tv_api_key = 'YOUR_TV_API_KEY'

# Set the TradingView account ID
tv_account_id = 'YOUR_TV_ACCOUNT_ID'

# Set the CoinMarketCap API URL
cmc_url = 'https://api.coinmarketcap.com/v1/ticker/'

# Set the CoinMarketCap API key
cmc_api_key = 'YOUR_CMC_API_KEY'

# Set the request headers
headers = {
    'Content-Type': 'application/json',
    'X-TV-API-KEY': tv_api_key,
    'X-CMC_PRO_API_KEY': cmc_api_key
}

# Set the request data
data = {
    'account_id': tv_account_id,
    'symbol': 'AAPL',
    'type': 'market',
    'side': 'buy',
    'quantity': 100
}

# Send the request to the TradingView API to create a new order
response = requests.post(tv_url + 'orders/new', headers=headers, data=json.dumps(data))

# Print the response from the TradingView API
print(response.text)

# Set the request parameters for the CoinMarketCap API
params = {
    'convert': 'USD'
}

# Send the request to the CoinMarketCap API to get the ticker information
response = requests.get(cmc_url, params=params, headers=headers)

# Parse the response from the CoinMarketCap API
data = json.loads(response.text)

# Print the response from the CoinMarketCap API
print(data)
