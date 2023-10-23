class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        resSet = set()
        def buildSubsets(subset: list = [], ptr= 0):
            if ptr == len(nums):
                resSet.add(tuple(subset.copy()))
                return
            subset.append(nums[ptr])
            buildSubsets(subset, ptr+1)
            subset.pop()
            buildSubsets(subset, ptr+1)
        buildSubsets()
        res = [list(i) for i in resSet]
        return res
    
S = Solution()
print(S.subsetsWithDup([1,2,3]))

