class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
        left = self.binary_search(nums[:low:], target)
        right = self.binary_search(nums[low::], target)

        if left != -1:
            return left
        elif right != -1:
            return low + right
        return -1

    def binary_search(self, nums, target):
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1
        
        