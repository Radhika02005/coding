# Day 01 – Best Time to Buy and Sell Stock 🟢
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Approach:
# - Use two pointers: left (l) and right (r), starting at index 0 and 1 respectively.
# - Iterate through the array:
#     - If prices[r] > prices[l], calculate profit = prices[r] - prices[l] and update max profit.
#     - If prices[r] < prices[l], move the left pointer to r (new lower buying price).
# - Increment right pointer on every iteration.
# - Return the maximum profit found.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
