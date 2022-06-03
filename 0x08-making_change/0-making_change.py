#!/usr/bin/python3
""" implements coin changes algorithm"""


def makeChange(coins, total):
    """ Args:
        @coins: array of coins
        @total: integer(amount to make changes to)
    """
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    if dp[total] == total + 1:
        return -1
    return dp[total]
