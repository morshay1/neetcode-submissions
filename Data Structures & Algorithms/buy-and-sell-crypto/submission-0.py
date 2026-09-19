class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        output = 0
        for i in range(1, len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
                continue
            elif minimum < prices[i]:
                if prices[i] - minimum > output:
                    output = prices[i] - minimum
            else:
                continue
            
        return output

