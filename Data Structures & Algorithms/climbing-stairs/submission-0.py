class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1

        while n > 1:
            temp = first 
            first = first + second
            second = temp

            n -= 1

        return first