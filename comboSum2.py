class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        def dfs(i: int = 0, subset:list[int] = [], total: int = 0):
            if total > target:
                return
            elif total == target:
                res.append(subset.copy())
                return
            elif i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, subset, total + candidates[i])
            subset.pop()
            curr = candidates[i]
            while i < len(candidates) and candidates[i] == curr:
                i += 1
            dfs(i, subset, total)
        dfs()
        return res
S = Solution()
print(S.combinationSum2([1,2,3,4,5], 8))
