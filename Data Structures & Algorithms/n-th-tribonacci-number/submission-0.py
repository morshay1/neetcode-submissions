class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1


        while n > 0:
            next_val = t0 + t1 + t2
            t0 = t1
            t1 = t2 
            t2 = next_val
            n -= 1

        return t0