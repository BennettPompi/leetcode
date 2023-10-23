class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        if len(nums) < 3:
            return max(nums)
        dp = [0] * (len(nums))
        dp[-1],dp[-2],dp[-3] = nums[-1],nums[-2], nums[-3] + nums[-1]
        for i in range(4, len(nums)+1):
            dp[-i] = max(dp[-i + 2], dp[-i+3])
        return max(dp[0],dp[1])
        """