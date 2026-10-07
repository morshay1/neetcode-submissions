class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # definatly a stack question
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens: 
            if token not in operators:
                stack.append(token)
            else:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(int(first) + int(second))
                elif token == '-':
                    stack.append(int(first) - int(second))
                elif token == '*':
                    stack.append(int(first) * int(second))
                elif token == '/':
                    stack.append(int(first) / int(second))
            
        return int(stack[-1])
                