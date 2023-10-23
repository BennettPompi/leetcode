class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        longest = 0
        lastSeen = {}
        while l < len(s)-longest:
            print(l, r, longest)
            if r == len(s):
                longest = max(longest, r-l)
                break

            if s[r] not in lastSeen:
                lastSeen[s[r]] = r
            elif s[r] in lastSeen and lastSeen[s[r]]>= l:
                longest = max(longest, r-l)
                l = lastSeen[s[r]]+1
                lastSeen[s[r]] = r
            r += 1
        return longest