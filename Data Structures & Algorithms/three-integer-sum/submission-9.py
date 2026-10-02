class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            list_result = self.twoSum(nums, -nums[i], i + 1)
            list_result = [lst + [nums[i]] for lst in list_result]
            output += list_result
        output = [tuple(sorted(lst)) for lst in output]    
        return [list(tup) for tup in list(set(output))]

    def twoSum(self, nums, target, low):
        output = []
        high = len(nums) - 1
        while low < high:
            if nums[low] + nums[high] == target:
                output.append([nums[low], nums[high]])
                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1
        return output
        

