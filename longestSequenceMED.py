class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        ALGORITHM:
            Put all nums in dictionary (key: num, value: 0 (longest subseq starting    
            with that num))
            for each key in dict, recursively search forward
                base case: key not in dict -> return 0
                if value is 0 -> return f(i) + 1
                if value > 0 -> return value
        """
        def searchForward(numsDict: dict[int, int], num: int):
            print(num)
            if num not in numsDict:
                return numsDict
            if numsDict[num] > 0:
                return numsDict
            numsDict = searchForward(numsDict, num+1)
            if num + 1 in numsDict:
                numsDict[num] = numsDict[num+1] + 1
            else:
                numsDict[num] = 1

            return numsDict
        
        numsDict = {}
        for n in nums:
            numsDict[n] = 0
        for k in numsDict.keys():
            searchForward(numsDict, k)
        print(numsDict)
        return max(numsDict.values())
        