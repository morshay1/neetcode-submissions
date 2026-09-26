class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        longest_str = ""

        for char in s:
            if char not in longest_str:
                longest_str += char
            else:
                char_index = longest_str.index(char)
                longest_str = longest_str[char_index + 1::] + char
            if len(longest_str) > longest:
                longest = len(longest_str)
        
        return longest
                































        
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
