class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_hash =  {}
        for i in range(len(nums)):
            diff_hash[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in diff_hash and i != diff_hash[nums[i]]:
                return [i, diff_hash[nums[i]]]
