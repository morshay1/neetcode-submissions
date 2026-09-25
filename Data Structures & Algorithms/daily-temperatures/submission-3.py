class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                element = stack.pop()
                output[element[1]] = i - element[1]
            stack.append((temperatures[i], i))
            

        return output
