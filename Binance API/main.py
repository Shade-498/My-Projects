import requests

# BTC Price
response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
print('Price:')
print(response.json()['price'])
