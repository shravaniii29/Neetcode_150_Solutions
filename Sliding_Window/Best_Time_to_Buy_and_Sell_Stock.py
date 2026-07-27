#You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.



def maxProfit(prices):

    buy = 0
    sell = 1

    max_profit = 0

    while sell < len(prices):

        if prices[sell] > prices[buy]:

            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)

        else:

            buy = sell

        sell += 1

    return max_profit


# Driver Code
n = int(input())

prices = list(map(int, input().split()))

print(maxProfit(prices))


# Approach:
# 1. Keep two pointers: buy and sell.
# 2. Buy always points to the minimum price seen so far.
# 3. Calculate profit whenever selling price is higher.
# 4. Update maximum profit.
#
# Time Complexity: O(n)
# Space Complexity: O(1)