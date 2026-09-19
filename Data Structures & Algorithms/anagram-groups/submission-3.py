import string
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def helper(s: str):
            eng_hash = {letter: 0 for letter in string.ascii_lowercase}
            for char in s:
                eng_hash[char] += 1
            return tuple(eng_hash.items())
        
        dic = defaultdict(list) # {: [], : []}
        for s in strs: # abc
            #   (("a", 1), ("b", 1), ...): ["abc", "bac"]
            dic[helper(s)].append(s)
        # {(()): ["sbc", "bcs"], (()): }
        return list(dic.values())

# "hello"
# (("a", 0), .... ("e", 1), ())