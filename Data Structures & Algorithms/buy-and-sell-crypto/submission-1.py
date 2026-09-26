class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stack = [prices[0]]

        for p in prices[1::]:
            if p < stack[-1]:
                stack.pop()
                stack.append(p)
            else: 
                profit = p - stack[-1]
                if profit > max_profit:
                    max_profit = profit
                

        return max_profit























        
        # minimum = prices[0]
        # output = 0
        # for i in range(1, len(prices)):
        #     if minimum > prices[i]:
        #         minimum = prices[i]
        #         continue
        #     elif minimum < prices[i]:
        #         if prices[i] - minimum > output:
        #             output = prices[i] - minimum
        #     else:
        #         continue
            
        # return output

