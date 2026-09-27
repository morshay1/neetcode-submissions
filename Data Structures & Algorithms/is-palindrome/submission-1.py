class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_letters = "qwertyuiopasdfghjklzxcvbnm0123456789"
        final_string = ""
        s = s.lower()
        for char in s:
            if char in valid_letters:
                final_string += char

        return final_string == final_string[::-1]























        
        # s = s.lower()
        # alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        # clean = ""
        # for char in s:
        #     if char in alphanumeric:
        #         clean += char
        # return clean == clean[::-1]