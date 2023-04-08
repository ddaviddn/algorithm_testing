from typing import List
from prometheus_client.decorator import __init__

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        print(f'Stock Array is: {prices}')

        lo_val = prices[0]
        profit = []

        for i in range(len(prices)):
            if lo_val > prices[i]:
                lo_val = prices[i]
            else:
                profit.append(prices[i] - lo_val)

        print('Max Profit you can get is: ')

        return max(profit)


if __name__ == '__main__':
    test_case1 = [7, 1, 5, 3, 6, 4]
    test_case2 = [7, 6, 4, 3, 2, 1]
    test_case3 = [2, 1]
    test_case4 = [1, 2]
    test_case5 = [2, 4, 1]

    print(Solution.maxProfit(__init__, prices=test_case1))
    print(Solution.maxProfit(__init__, prices=test_case2))
    print(Solution.maxProfit(__init__, prices=test_case3))
    print(Solution.maxProfit(__init__, prices=test_case4))
    print(Solution.maxProfit(__init__, prices=test_case5))
