class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(coin_index, amount):
            if amount == 0:
                return 0

            if coin_index == len(coins):
                return float('inf')

            if (coin_index, amount) in memo:
                return memo[(coin_index, amount)]
            
            dont_take = helper(coin_index + 1, amount)
            take = float('inf')
            if coins[coin_index] <= amount:
                take = 1 + helper(coin_index, amount - coins[coin_index])    

            res = min(take, dont_take)
            memo[(coin_index, amount)] = res
            return res
        
        answer = helper(0, amount)
        return -1 if answer == float('inf') else answer
        

    
        