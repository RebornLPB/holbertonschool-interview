#!/usr/bin/python3
"""Compute the minimum number of coins needed to reach a total."""


def makeChange(coins, total):
    """Return the fewest coins needed to make the specified total.

    Args:
        coins: Iterable of positive coin denominations.
        total: Amount to make.

    Returns:
        The minimum number of coins, or -1 if the total cannot be made.
        Returns 0 when total is zero or negative.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
