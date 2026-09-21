class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        if self.k > len(self.nums):
            index = self.binary_search(self.nums, val)
            self.nums.insert(index, val)
            return self.nums[0]
        if val < self.nums[-self.k]:
            self.nums = [val] + self.nums
            return self.nums[-self.k]
        else:
            index = self.binary_search(self.nums[-self.k:], val)
            self.nums.insert(len(self.nums) - self.k + index, val)
            return self.nums[-self.k]  

        
    def binary_search(self, nums, val) -> int:
        low = 0 
        high = len(nums)
        while low < high:
            mid = (high + low) // 2
            if nums[mid] == val:
                return mid
            elif nums[mid] < val:
                low = mid + 1
            else:
                high = mid
        return low
