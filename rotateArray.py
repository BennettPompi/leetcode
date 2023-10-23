class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotNums = [None] * n
        for i in range(n):
            pos = i + k
            if ((i + k) > n):
                pos = pos%n
            rotNums[pos] = nums[i]
        for i in range(n):
            nums[i] = rotNums[i]