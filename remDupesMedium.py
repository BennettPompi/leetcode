class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        n = len(nums)
        if n == 2 or nums[0] == nums[n-1]:
            return 2
        while j < n:
            if (nums[i + 2] <= nums[i]):
                if j == 0:
                    j = i+2
                while j < n and nums[j] <= nums[i]:
                    j += 1
                if j == n:
                    return i + 2
                nums[i+2] = nums[j]
                nums[j] = 0
            else:
                j = i+2
            i += 1
        return i + 2