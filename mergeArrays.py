class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        writeIndex = m + n - 1
        it1 = m-1
        it2 = n-1

        while(it2 >= 0):
            if(it1 >= 0 and nums1[it1] >= nums2[it2]):
                nums1[writeIndex] = nums1[it1]
                it1 -= 1
            else:
                nums1[writeIndex] = nums2[it2]
                it2 -= 1
            writeIndex -= 1