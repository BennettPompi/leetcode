class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []
        string = ""
        def recursiveSolution(stack: list[chr], n:int, lCount:int, string:str, result:list[str]):
            if not stack and lCount == n:
                result.append(string)
                return
            if not stack:
                stack.append('(')
                string += '('
                lCount += 1
                recursiveSolution(stack, n, lCount, string, result)
            else:
                closeCpStack = stack.copy()
                closeCpStr = string
                closeCpStr += ')'
                closeCpStack.pop()
                recursiveSolution(closeCpStack, n, lCount, closeCpStr, result)
                if lCount != n:
                    string += '('
                    stack.append('(')
                    lCount+=1
                    recursiveSolution(stack, n, lCount, string, result)
            return
        recursiveSolution(stack, n, 0, string, res)
        