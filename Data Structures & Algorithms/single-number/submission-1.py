class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = nums[0]
        for i in range(1, len(nums)):
            single = nums[i] ^ single

        return single


























        
        # res = nums[0]
        # for num in nums[1::]:
        #     res = res ^ num
        # return res

