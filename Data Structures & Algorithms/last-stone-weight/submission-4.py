class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            sec_heaviest = heapq.heappop_max(stones)
            diff = heaviest - sec_heaviest 
            if diff > 0:
                heapq.heappush_max(stones, diff)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]



        # l = len(stones)

        # while l > 1:
        #     stones.sort(reverse=True)
        #     if stones[0] == stones[1]:
        #         stones = stones[2::]
        #     else:
        #         stones[0] -= stones[1]
        #         stones.pop(1)
        #     l = len(stones)
        # if l == 0:
        #     return 0
        # else:
        #     return stones[0]
    
