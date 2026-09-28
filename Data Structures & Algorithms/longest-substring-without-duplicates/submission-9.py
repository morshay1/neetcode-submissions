class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        max_sub = ""
        
        for i in range(len(s)):
            if s[i] not in max_sub:
                max_sub += s[i]
            else:
                idx = max_sub.index(s[i])
                max_sub = max_sub[idx + 1::] + s[i]
            if len(max_sub) > max_len:
                max_len = len(max_sub)
        
        return max_len


























        # longest = 0
        # longest_str = ""

        # for char in s:
        #     if char not in longest_str:
        #         longest_str += char
        #     else:
        #         char_index = longest_str.index(char)
        #         longest_str = longest_str[char_index + 1::] + char
        #     if len(longest_str) > longest:
        #         longest = len(longest_str)
        
        # return longest
                































        
        # longest_len = 0
        # current_len = 0
        # visited = ""

        # for char in s:
        #     if char not in visited:
        #         visited += char
        #         current_len += 1
        #     else:
        #         seen_index = visited.find(char)
        #         visited = visited[seen_index + 1::] + char
        #         current_len = len(visited)
        #     if current_len > longest_len:
        #         longest_len = current_len
        # return longest_len
