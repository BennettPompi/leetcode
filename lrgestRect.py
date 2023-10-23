class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []
        for i,h in enumerate(heights):
            if not stack or stack[-1][0] <= h:
                stack.append((h, i))
            else:
                last = None
                while stack and stack[-1][0] > h:
                    last = stack.pop()
                    maxArea = max(maxArea, (last[0] * (i-last[1])))
                stack.append((h, last[1]))
        for x in stack:
            area = x[0] * (len(heights)-x[1])
            maxArea = max(area, maxArea)
        return maxArea