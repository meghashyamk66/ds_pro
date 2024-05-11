import requests

def get_stock_price(symbol):
    api_key = 'sk-proj-UnMEeSR6EciBnbtmBw05T3BlbkFJQrfINoyrqPfbWkwHo1SE'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data and '05. price' in data['Global Quote']:
        return data['Global Quote']['05. price']
    else:
        return None

# Take input from the user
stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple Inc.): ").upper()

# Get the stock price
price = get_stock_price(stock_symbol)
if price:
    print(f"The current price of {stock_symbol} is ${price}")
else:
    print("Failed to retrieve stock price. Please check the stock symbol.")