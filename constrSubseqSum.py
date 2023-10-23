from heapq import heappop,heappush
class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        res = nums[0]
        for i in range(1,len(nums)):
            while i- heap[0][1] > k:
                heappop(heap)
            opt = min(heap[0][1], 0)-nums[i]
            if -opt > res:
                res = opt
            heappush(heap, (opt, i))
        return res
S = Solution()
print(S.constrainedSubsetSum([1,2,-3,4,5],1))


