class Solution:
   
    def maxArea(self, height: list[int]) -> int:
        """
        algorithm:
        see if you can raise min height
        if you can, see if distance traveled in is < (newMin-oldMin)
        if yes, update max area found
        else, keep going
        terminate when i >= j
        return area of max
        """
        #height = [1,8,6,2,5,4,8,3,7]
        if len(height) == 2:
            return min(height[0], height[1])
        i,j = 0, len(height)-1
        maxLeft = i
        maxRight = j
        waterLine = min(height[maxLeft], height[maxRight])
        maxArea = (maxRight-maxLeft)*waterLine

        while i < j:
            if height[i] < height[j]:
                while height[i] <= waterLine and i < j:
                    i += 1
            elif height [i] > height[j]:
                while height[j] <= waterLine and i <j:
                    j -=1
            else:
                while height[i] == height[j] and i < j:
                    i -= 1
                    j -= 1
            if i < j and maxArea < (min(height[i], height[j])*(j-i)):
                maxLeft = i
                maxRight = j
                waterLine = min(height[maxLeft], height[maxRight])
                maxArea = (maxRight-maxLeft)*waterLine

        return maxArea