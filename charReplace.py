class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0

        charCounts = {}

        for r in range(len(s)):
            charCounts[s[r]] = charCounts.get(s[r], 0) + 1

            while (r-l + 1) - max(charCounts.values()) > k:
                charCounts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res


