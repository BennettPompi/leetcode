"""
Leetcode 79: Word Search
Takes board of the form
[
    [a,b,c,d,e,f,g]
    [a,b,c,d,e,f,g]
    [a,b,c,d,e,f,g]
    ....
    [a,b,c,d,e,f,g]
    [a,b,c,d,e,f,g]
    [a,b,c,d,e,f,g]
    ....
]
and searches for string
"""



from collections import defaultdict
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def getNeighbors(x, y):
            neighbors =[]
            if y > 0:
                neighbors.append((board[y-1][x], x, y-1))
            if y < len(board)-1:
                neighbors.append((board[y+1][x], x, y+1))
            if x > 0:
                neighbors.append((board[y][x-1], x-1, y))
            if x < len(board[0])-1:
                neighbors.append((board[y][x+1], x+1, y))
            return neighbors
        def dfs(col, row, pos=0)-> bool:
            if pos == len(word)-1 and board[row][col] == word[-1]:
                return True
            neighbors = getNeighbors(col, row)
            for n in neighbors:
                if n[0] == word[pos+1] and usedDict[n] == False:
                    print(n)
                    usedDict[n] = True
                    found = dfs(n[1],n[2],pos+1)
                    usedDict[n] = False
                    if found:
                        return True
            return False

        usedDict = defaultdict(lambda: False)
        for row in range(len(board)):
            for col, c in enumerate(board[row]):
                if c != word[0]:
                    continue
                else:
                    start = (c, col, row)
                    usedDict[start] = True
                    if dfs(col, row):
                        return True
                    usedDict[start] = False
        return False

S = Solution()
print(S.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
                    
                    

            
            