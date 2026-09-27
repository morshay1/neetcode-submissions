class Solution:
    def isValid(self, s: str) -> bool:  
        par = ["()", "[]", "{}"] 
        openeing_par = ["(", "[", "{"]
        stack = []
        par_hash = {}
        for char in par:
            par_hash[char[1]] = char[0]

        for par in s:
            if par in openeing_par:
                stack.append(par)
            else:
                if len(stack) == 0:
                    return False
                if par_hash[par] == stack[-1]:
                    stack.pop()
                else:
                    return False        
        return len(stack) == 0

        

























        
           
        # validness_stack = []
        # opening_parentheses = ["[", "{", "("]

        # parentheses_hash = {}
        # valid_parentheses = ["[]", "()", "{}"]
        # for parentheses in valid_parentheses:
        #     parentheses_hash[parentheses[1]] =  parentheses[0]
            
        # for char in s:
        #     if char in opening_parentheses:
        #         validness_stack.append(char)
        #     else:
        #         if len(validness_stack) == 0:
        #             return False
        #         if validness_stack[-1] == parentheses_hash[char]:
        #             validness_stack.pop()
        #         else:
        #             return False
            
        # if len(validness_stack) == 0:
        #     return True
        # return False
