class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result =[0*len(temperatures)]
        for i,x in enumerate(temperatures):
            while stack and x > stack[-1][0]:
                result[i] = (i - stack[-1][1])
                stack.pop()
            stack.append((x, i))
        return result

        