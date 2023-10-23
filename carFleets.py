class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        tuples = [None]*len(position)
        for i, x in enumerate(position):
            eta = (target-x)/speed[i]
            tuples[i] = (x, eta)
        tuples.sort(key=lambda a: a[0])
        for i,x in enumerate(tuples):
            while stack and x[1] >= stack[-1][1]:
                stack.pop()
            stack.append(x)
        return len(stack)