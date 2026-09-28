from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
            
        min_hash = []
        heapq.heapify(min_hash)
        for key, value in counts.items():
            heapq.heappush(min_hash, (value, key))
        
        while len(min_hash) - k > 0:
            heapq.heappop(min_hash)[1]

        for element in min_hash:
            output.append(element[1])
        return output
        

























        
        # freq_hash = {}
        # for num in nums:
        #     if num in freq_hash:
        #         freq_hash[num] += 1
        #     else:
        #         freq_hash[num] = 0
        # heap = [(value, key) for key, value in freq_hash.items()]
        # heapq.heapify_max(heap)
        # output = []
        # while k > 0:
        #     max_num = heapq.heappop_max(heap)
        #     output.append(max_num[1]) 
        #     k -= 1
        # return output