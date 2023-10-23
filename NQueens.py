class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #let 0 indicate that a space is empty, -1 that that space is being attacked, and 1 that a queen has been placed there
        #for each row of n 
        board = [[0]*n]*n
        