class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums) - 1
        i = 0

        while i < k:
            while (nums[i] == val):
                nums.pop(i)
                k-= 1
                if (i > k):
                    break
            i += 1