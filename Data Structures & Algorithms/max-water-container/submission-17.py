class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low, high = 0, len(heights) - 1
        max_water = 0
        
        while low < high:
            curr_water = min(heights[low], heights[high]) * (high - low)
            if heights[low] < heights[high]:
                low += 1
            elif heights[low] > heights[high]:
                high -= 1
            else:
                low += 1
                high -= 1
            if max_water < curr_water:
                max_water = curr_water
            print(low)
        return max_water











        # water_per_bar = [0] * len(heights)
        # for i in range(len(heights)):
        #     max_length_forward = 0
        #     max_length_backwards = 0
        #     j= i + 1
        #     k = i - 1
        #     while j < len(heights):
        #         if heights[j] >= heights[i]:
        #             max_length_forward = j - i
        #         j += 1
        #     while k > -1:
        #         if heights[k] >= heights[i]:
        #             max_length_backwards = i - k
        #         k -= 1
        #     water_per_bar[i] = max(heights[i] * max_length_forward,
        #                             heights[i] * max_length_backwards)
        # return max(water_per_bar)