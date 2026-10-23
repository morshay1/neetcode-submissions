class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {} # (k, i): False

        def helper(k, i): # memo
            if i == len(nums) - 1:
                return k == nums[i]
            
            if (k - nums[i], i + 1) not in memo:
                memo[(k - nums[i], i + 1)] = helper(k - nums[i], i + 1)
            if (k + nums[i], i + 1) not in memo:
                memo[(k + nums[i], i + 1)] = helper(k + nums[i], i + 1)
            return memo[(k - nums[i], i + 1)] or memo[(k + nums[i], i + 1)]

        return helper(0, 0)