class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        take = self.subsets(nums[1::])
        take = [[nums[0]] + lst for lst in take] 
        dont_take = self.subsets(nums[1::])

        return take + dont_take






























        
        # understand the list comprehension 
        # if len(nums) == 0:
        #     return [[]]
        
        # prev = self.subsets(nums[1::])
        # return prev + [[nums[0]] + x for x in prev] 

        # dont_take = self.subsets(nums[1::])
        # take = []
        # for sub in dont_take:
        #     new_subset = [nums[0]] + sub
        #     take.append(new_subset)
        
        # return take + dont_take


        