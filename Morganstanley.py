import json
import requests
import time

URL = "http://fx-trading-game-leicester-challenge.westeurope.azurecontainer.io:443/"
TRADER_ID = "NWyvtpxYuLqlmTXVFKwgyKfmvD5g5RV0"

class Side:
    BUY = "buy"
    SELL = "sell"


def get_price():
    api_url = URL + "/price/EURGBP"
    res = requests.get(api_url)
    if res.status_code == 200:
        return json.loads(res.content.decode('utf-8'))["price"]
    return None


def trade(trader_id, qty, side):
    api_url = URL + "/trade/EURGBP"
    data = {"trader_id": trader_id, "quantity": qty, "side": side}
    res = requests.post(api_url, json=data)
    if res.status_code == 200:
        resp_json = json.loads(res.content.decode('utf-8'))
        if resp_json["success"]:
            return resp_json["price"]
    return None


def trade_history():
    api_url = URL + "/tradeHistory"
    res = requests.get(api_url)
    if res.status_code == 200:
        resp_json = json.loads(res.content.decode('utf-8'))
        print(resp_json)
    return None


def get_inventory(trader_id):
    api_url = URL + "/positions/" + trader_id
    response = requests.get(api_url)
    if response.status_code == 200:
        resp_json = json.loads(response.content.decode('utf-8'))
        print(resp_json)
    return None


def simple_moving_average(prices, window_size):
    if len(prices) >= window_size:
        return sum(prices[-window_size:]) / window_size
    return None


def trading_strategy():
    window_size = 3  # Define the moving average window size
    prices = []

    while True:
        current_price = get_price()
        if current_price is not None:
            prices.append(current_price)

            # Ensure we have enough data to compute the moving average
            if len(prices) >= window_size:
                sma = simple_moving_average(prices, window_size)

                # Trading logic based on the moving average
                if current_price > sma:
                    # If the current price is above the moving average, we might consider buying
                    print(f"Price {current_price} is above the moving average {sma}. Buying EUR.")
                    trade(TRADER_ID, 3000, Side.BUY)

                elif current_price < sma:
                    # If the current price is below the moving average, we might consider selling
                    print(f"Price {current_price} is below the moving average {sma}. Selling EUR.")
                    trade(TRADER_ID, 100, Side.SELL)

            else:
                print(f"Collecting price data, current list: {prices}")

        get_inventory(TRADER_ID)

        time.sleep(1)

if __name__ == '__main__':
    print("Expected to trade at:" + str(get_price()))
    get_inventory(TRADER_ID)
    trade_history()

    #momentum_strategy()
    trading_strategy()
