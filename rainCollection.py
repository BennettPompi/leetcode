class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        left = 0
        right = len(height)-1
        maxLeft = height[left]
        maxRight = height[right]
        area = 0

        while left < right:
            if height[left] <= height[right]:
                left += 1
                if maxLeft < height[left]:
                    maxLeft = height[left]
                if height[left] < min(maxLeft, maxRight):
                    area += min(maxLeft, maxRight) - height[left]

            else:
                right -= 1
                if maxRight < height[right]:
                    maxRight = height[right]
                if height[right] < min(maxLeft, maxRight):
                    area += min(maxLeft, maxRight) - height[right]
        return area