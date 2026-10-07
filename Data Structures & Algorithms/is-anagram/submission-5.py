from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_hash = defaultdict(int)

        for char in s:
            count_hash[char] += 1
        
        for char in t:
            if char not in count_hash:
                return False
            count_hash[char] -= 1
        
        for key in count_hash:
            if count_hash[key] != 0:
                return False
        return True





























        # count_hash = {}

        # for char in s:
        #     if char not in count_hash:
        #         count_hash[char] = 0
        #     count_hash[char] += 1
        
        # for char in t:
        #     if char not in count_hash:
        #         return False
        #     count_hash[char] -= 1

        # for key, value in count_hash.items():
        #     if value != 0:
        #         return False
        # return True























        
        # hash_string = {}
        # for char in s:
        #     if char not in hash_string:
        #         hash_string[char] = 0
        #     hash_string[char] += 1
        # for char in t:
        #     if char not in hash_string:
        #         return False
        #     hash_string[char] -= 1
        # for element in hash_string:
        #     if hash_string[element] != 0:
        #         return False
        # return True