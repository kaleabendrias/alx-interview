#!/usr/bin/python3
"""determine the fewest number of coins needed to meet a given"""
def makeChange(coins, total):
    """Create a list to store the minimum number of coins needed"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
