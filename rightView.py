# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, lvl, arr):
        if not root:
            return
        if lvl == len(arr):
            arr.append(root.val)
        self.dfs(root.right,lvl+1, arr)
        self.dfs(root.left, lvl+1, arr)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        return res
        
            


        
        