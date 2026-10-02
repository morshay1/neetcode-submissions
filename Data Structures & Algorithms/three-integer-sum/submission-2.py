class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        new_nums = nums.copy()
        for i in range(len(nums)):
            num = new_nums.pop(i)
            list_result = self.twoSum(new_nums, -num)
            list_result = [lst + [num] for lst in list_result]
            output += list_result
            new_nums.insert(i, num)
        output = [tuple(sorted(lst)) for lst in output]    
        return [list(tup) for tup in list(set(output))]

    def twoSum(self, nums, target):
        output = []
        low, high = 0, len(nums) - 1
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
        

