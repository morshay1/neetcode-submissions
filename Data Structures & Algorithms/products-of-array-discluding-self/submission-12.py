class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        zeros = nums.count(0)

        mul = 1
        for num in nums:
            if num == 0:
                idx = nums.index(0)
                continue
            mul *= num
        
        if zeros == 1:
            output[idx] = mul 
            return output

        if zeros == 0:
            for i in range(len(nums)):
                output[i] = mul // nums[i]
        return output



        # n = len(nums)
        # output = [0] * n

        # for i in range(n):
        #     mul = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         mul *= nums[j]
        #     output[i] = mul
        
        # return output

            





























        
        # output = [0] * len(nums)
        # total_sum = 1

        # for num in nums:
        #     if num != 0:
        #         total_sum *= num
        
        # zeros_count = nums.count(0)
        # if zeros_count == 0:
        #     for i in range(len(nums)):
        #         output[i] = total_sum // nums[i]

        # elif zeros_count == 1:
        #     zero_index = nums.index(0)
        #     output[zero_index] = total_sum

        # return output

        # output = []
        # prefix = [0] * len(nums)
        # suffix = [0] * len(nums)      
        # for i in range(len(nums)):
        #     if i == 0:
        #         output.append(suffix[i])
        #     elif i == len(nums) - 1:
        #         output.append(prefix[i])
        #     else:
        #         output.append(prefix[i] * suffix[i])               

        # return output