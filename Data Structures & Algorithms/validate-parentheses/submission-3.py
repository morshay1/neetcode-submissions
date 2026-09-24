class Solution:
    def isValid(self, s: str) -> bool:       
        validness_stack = []
        opening_parentheses = ["[", "{", "("]

        parentheses_hash = {}
        valid_parentheses = ["[]", "()", "{}"]
        for parentheses in valid_parentheses:
            parentheses_hash[parentheses[1]] =  parentheses[0]
            
        for char in s:
            if char in opening_parentheses:
                validness_stack.append(char)
            else:
                if len(validness_stack) == 0:
                    return False
                if validness_stack[-1] == parentheses_hash[char]:
                    validness_stack.pop()
                else:
                    return False
            
        if len(validness_stack) == 0:
            return True
        return False
