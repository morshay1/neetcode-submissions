class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_hash = {}

        for num in nums:
            if num not in count_hash:
                count_hash[num] = 0
            count_hash[num] += 1

        for key, value in count_hash.items():
            if value > 1:
                return True
        return False


























        
        # dup_hash = {}
        # for num in nums: 
        #     if num in dup_hash:
        #         return True
        #     dup_hash[num] = False
        # return False