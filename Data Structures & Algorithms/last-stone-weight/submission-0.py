class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = len(stones)
        while l > 1:
            stones.sort(reverse=True)
            print(len(stones))
            print(stones[0])
            if stones[0] == stones[1]:
                stones = stones[2::]
            else:
                stones[0] -= stones[1]
                stones.pop(1)
            l = len(stones)
        if l == 0:
            return 0
        else:
            return stones[0]
