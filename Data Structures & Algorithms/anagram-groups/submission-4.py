import string
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        letters_count_hash_to_index_hash = {}
        for s in strs:
            letters_count_hash = {letter: 0 for letter in string.ascii_lowercase}
            for char in s:
                if char not in letters_count_hash:
                    letters_count_hash[char] = 0
                letters_count_hash[char] += 1
            # for word 'act' for example:
            # letters_count_hash = {a: 1, c: 1, t: 1}
            lch = tuple(letters_count_hash.items()) # (('a', 1), ('c', 1), ('t', 1))
            if lch not in letters_count_hash_to_index_hash:
                letters_count_hash_to_index_hash[lch] = [s]
            else:
                letters_count_hash_to_index_hash[lch].append(s) 

        return list(letters_count_hash_to_index_hash.values())
            
            

























        # def helper(s: str):
        #     eng_hash = {letter: 0 for letter in string.ascii_lowercase}
        #     for char in s:
        #         eng_hash[char] += 1
        #     return tuple(eng_hash.items())
        
        # dic = defaultdict(list) # {: [], : []}
        # for s in strs: # abc
        #     #   (("a", 1), ("b", 1), ...): ["abc", "bac"]
        #     dic[helper(s)].append(s)
        # # {(()): ["sbc", "bcs"], (()): }
        # return list(dic.values())

