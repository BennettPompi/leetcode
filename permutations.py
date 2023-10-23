class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(curr:list[int] = [], choices:list[int] = nums):
            if not choices:
                res.append(curr.copy())
            for x in choices:
                curr.append(x)
                dfs(curr, [i for i in choices if i != x])
                curr.pop()
        dfs()
        return res
S = Solution()
print(S.permute([1,2,3]))

            