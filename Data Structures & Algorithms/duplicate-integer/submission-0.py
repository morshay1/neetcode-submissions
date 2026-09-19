class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_hash = {}
        for num in nums: 
            if num in dup_hash:
                return True
            dup_hash[num] = False
        return False