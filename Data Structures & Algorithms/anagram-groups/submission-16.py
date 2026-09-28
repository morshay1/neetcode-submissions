from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # {key:[], key:[]}

        for s in strs: # s for example is 'cat'
            count = [0] * 26 # count = [000000..] 0 appears 26 times

            for char in s:
                count[ord(char) - ord('a')] += 1 # ord('a') = 97 (a is 97 by ascii) 
                                                # count = [1, 0, 1, 0, ..., 1, ...]

            groups[tuple(count)].append(s) # {(1, 0, 1, 0, ..., 1, ...): ["cat", "act"],
                                            # (1, 1, 0, 0, ..., 1, ...): ["bat", "tab"]}

        return list(groups.values()) #[[cat, act], ...]            
            

























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

