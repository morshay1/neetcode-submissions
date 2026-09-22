class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        current_len = 0
        visited = ""

        for char in s:
            if char not in visited:
                visited += char
                current_len += 1
            else:
                seen_index = visited.find(char)
                visited = visited[seen_index + 1::] + char
                current_len = len(visited)
            if current_len > longest_len:
                longest_len = current_len
        return longest_len
