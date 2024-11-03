# Morgan-Stanley-Coding-Challenge
FX Trading Game Bot
This Python script implements a basic trading bot for the FX Trading Game (EUR/GBP), using a simple moving average strategy to inform buy/sell decisions. The bot aims to maximise profit from an initial portfolio balance of $1,000,000 by identifying price trends and acting based on short-term market movements.

Overview
The bot continuously retrieves the current EUR/GBP exchange rate and calculates a moving average over a specified window (e.g., 3 data points). Using this average, the bot compares the current price to the average price over the window. If the price is above the moving average, the bot signals a potential upward trend and initiates a buy trade; if the price falls below the average, it signals a potential downtrend, prompting a sell trade.

Key Components
Price Fetching (get_price)
Retrieves the latest EUR/GBP price from the API. This function is called at regular intervals to keep the bot updated on price changes.

Trade Execution (trade)
Executes a buy or sell order depending on the strategy’s signals. Each trade request includes the trade quantity and the side (buy/sell).

Inventory Check (get_inventory)
Fetches the current inventory status to track holdings after each trade, displaying the bot’s position in EUR/GBP.

Trade History (trade_history)
Retrieves the history of all trades executed, allowing for performance analysis and debugging.

Simple Moving Average Calculation (simple_moving_average)
Calculates the average of the last few prices (specified by window_size) to determine the general price trend.

Trading Strategy (trading_strategy)
The main loop of the bot, which:

Retrieves the current price.
Appends each price to a list.
Calculates the simple moving average once there’s enough data.
Executes a buy if the price is above the moving average or a sell if the price is below.
How to Run
Ensure you have Python installed, along with the required packages (requests and json, which are part of the standard library).

Update the TRADER_ID with your own unique trader ID.

Execute the bot by running:

bash
Copy code
python trading_bot.py
The bot will continuously monitor and trade based on the moving average strategy, logging its actions and the inventory after each trade.

Strategy Explanation
The moving average strategy is a trend-following approach:

Buy Signal: When the current price is above the moving average, it indicates a possible upward trend, suggesting a good time to buy.
Sell Signal: When the current price falls below the moving average, it suggests a downtrend, prompting a sell to minimize potential losses.
Winning Strategy Explanation
To maximise profit from the initial $1,000,000 balance:

Optimal Position Size: Large buy positions (3000 units) are taken to capitalise on upward trends, while smaller sell positions (100 units) help control risk when the price falls.
Risk Control: The moving average window smooths short-term fluctuations, helping to avoid impulsive trades. This way, the bot balances between maximising gains and minimising exposure to downtrends.
By continually updating its position based on the latest price movements, this strategy aims to increase the overall portfolio value through incremental gains while maintaining a steady position size that aligns with the trading budget.

Future Improvements
Consider the following enhancements for potentially higher returns:

Implementing additional indicators for confirmation signals.
Adjusting the moving average window dynamically based on market volatility.
Adding stop-loss and take-profit mechanisms to secure profits and limit potential losses.
