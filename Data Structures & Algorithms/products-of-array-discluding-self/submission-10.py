class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        total_sum = 1

        for num in nums:
            if num != 0:
                total_sum *= num
        
        zeros_count = nums.count(0)
        if zeros_count == 0:
            for i in range(len(nums)):
                output[i] = total_sum // nums[i]

        elif zeros_count == 1:
            zero_index = nums.index(0)
            output[zero_index] = total_sum

        return output

        # output = []
        # prefix = []
        # suffix = len(nums)

        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix.append(0)
        #         suffix.insert(0, 0)
        #     elif i == 1:
        #         prefix.append(nums[0])
        #         suffix.insert(0, nums[-1])
        #     else:
        #         prefix.append(nums[i - 1] * prefix[i - 1])
        #         suffix.insert(0, nums[len(nums) - i] * suffix[0])                

        # for i in range(len(nums)):
        #     if i == 0:
        #         output.append(suffix[i])
        #     elif i == len(nums) - 1:
        #         output.append(prefix[i])
        #     else:
        #         output.append(prefix[i] * suffix[i])               

        # return output