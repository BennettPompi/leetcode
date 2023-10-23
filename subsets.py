#this is right but problem with res being same list across recursive calls. Fix when less tired.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def buildSubsets(nums, subset: list, ptr= 0, res = res):
            if ptr == len(nums):
                res.append(subset)
                return
            nonDup = ptr
            while nonDup < len(nums) and nums[ptr] == nums[nonDup]:
                nonDup += 1
            buildSubsets(nums, subset.copy(), nonDup)
            subset.append(nums[ptr])
            buildSubsets(nums, subset.copy(), ptr +1)
        
        buildSubsets(nums, [], 0)
        return res