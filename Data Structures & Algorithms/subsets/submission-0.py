class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        dont_take = self.subsets(nums[1::])
        take = []
        for sub in dont_take:
            new_subset = [nums[0]] + sub
            take.append(new_subset)
        
        return take + dont_take
