class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        l = 0
        max_area = 0
        r = n - 1
        while l < r:
            width = r - l
            min_height = min(heights[l], heights[r])
            area = min_height * width
            max_area = max(max_area , area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area