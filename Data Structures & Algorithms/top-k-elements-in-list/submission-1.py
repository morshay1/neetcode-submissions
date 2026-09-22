class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash = {}
        for num in nums:
            if num in freq_hash:
                freq_hash[num] += 1
            else:
                freq_hash[num] = 0
        heap = [(value, key) for key, value in freq_hash.items()]
        heapq.heapify_max(heap)
        output = []
        while k > 0:
            max_num = heapq.heappop_max(heap)
            output.append(max_num[1]) 
            k -= 1
        return output