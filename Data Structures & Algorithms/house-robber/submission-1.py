class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_money, max0, max1 = 0, nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            max_money = max(max0 + nums[i], max1)
            max0 = max1
            max1 = max_money

        return max1
