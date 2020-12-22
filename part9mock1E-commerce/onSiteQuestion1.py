"""

On-Site Question 1
Problem
You've been given a list of historical stock prices for a single day for Amazon stock. The index of the list represents
 the timestamp, so the element at index of 0 is the initial price of the stock, the element at index 1 is the next
 recorded price of the stock for that day, etc. Your task is to write a function that will return the maximum profit
 possible from the purchase and sale of a single share of Amazon stock on that day. Keep in mind to try to make this
 as efficient as possible.

"""


def profit(stock_prices):

    # Start minimum prices marker at first price
    min_stock_price = stock_prices[0]

    # Start off with a profit of zero
    max_profit = 0

    for price in stock_prices:

        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price, price)

        # Check the current price against our minimum for a profit
        # comparison against the max_profit
        comparison_profit = price - min_stock_price

        # Compare against our max_profit so far
        max_profit = max(max_profit, comparison_profit)

    return max_profit


print(profit([10, 12, 14, 12, 13, 11, 8, 7, 6, 13, 23, 45, 11, 10]))
