class Solution:
    def climbStairs(self, n: int) -> int:
        fib_first, fib_sec = 1, 1

        i = 1
        while i < n:
            temp = fib_first
            fib_first = fib_first + fib_sec
            fib_sec = temp
            i += 1

        return fib_first
























        # first = 1
        # second = 1

        # while n > 1:
        #     temp = first 
        #     first = first + second
        #     second = temp

        #     n -= 1

        # return first