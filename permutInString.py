class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #dictionary: key->character, value->count
        left = 0
        charCounts = {}
        for c in s1:
            charCounts[c] = charCounts.get(c, 0) +1
        
        for right, char in enumerate(s2):
            if char not in charCounts:
                while left < right+1:
                    if s2[left] in charCounts:
                        charCounts[s2[left]] += 1
                    left += 1
                continue
            if char in charCounts:
                charCounts[char] -= 1

            if charCounts[char] < 0:
                while charCounts[char] < 0:
                    if s2[left] in charCounts:
                        charCounts[s2[left]] += 1
                    left += 1
            windowSize = right - left + 1
            if windowSize == len(s1):
                return True
        return False
            