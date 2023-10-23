class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majNum = nums[0]
        k=0
        for x in nums:
            if x == majNum:
                k += 1
            else:
                k -= 1
                if k == 0:
                    majNum = x
                    k += 1
        return majNum