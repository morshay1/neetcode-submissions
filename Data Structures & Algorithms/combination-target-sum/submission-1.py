class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 1:
            if target % nums[0] == 0:
                return [[nums[0]] * (target // nums[0])]
            else:
                return []
        if nums[0] > target:
            use = []
        else:        
            use = self.combinationSum(nums, target - nums[0])
            use = [[nums[0]] + lst for lst in use]
        dont_use = self.combinationSum(nums[1::], target)
    
        return use + dont_use

































        
        # if len(nums) == 1:
        #     return [[nums[0]] * (target // nums[0])] if target % nums[0] == 0 else []
        # if target < nums[0]:
        #     use = []
        # else:
            
        #     use = self.combinationSum(nums, target - nums[0])
        #     use = [[nums[0]] + lst for lst in use]
        # dont_use = self.combinationSum(nums[1::], target)
        
        # return use + dont_use
