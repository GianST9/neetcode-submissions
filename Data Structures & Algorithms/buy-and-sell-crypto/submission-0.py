class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i, price in enumerate(prices):
            balance = max(prices[i:]) - prices[i] 
            if balance > output:
                output = balance
        

        return output