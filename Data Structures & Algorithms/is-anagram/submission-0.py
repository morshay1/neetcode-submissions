class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_string = {}
        for char in s:
            if char not in hash_string:
                hash_string[char] = 0
            hash_string[char] += 1
        for char in t:
            if char not in hash_string:
                return False
            hash_string[char] -= 1
        for element in hash_string:
            if hash_string[element] != 0:
                return False
        return True