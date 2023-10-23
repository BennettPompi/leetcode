class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res =[]
        def findCombos(pos: int = 0, combo: list[int] = [], total = 0):
            if total == target:
                    res.append(combo.copy())
                    return
            if total > target or pos == len(candidates):
                return
            findCombos(pos+1, combo, total)
            combo.append(candidates[pos])
            findCombos(pos, combo, total + candidates[pos])
            combo.pop()
            
        findCombos()
        return res
            

sol = Solution()
print(sol.combinationSum([1,2,3,4],10))