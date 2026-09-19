class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        clean = ""
        for char in s:
            if char in alphanumeric:
                clean += char
        return clean == clean[::-1]