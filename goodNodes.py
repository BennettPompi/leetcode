# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, maxVal):
        if not root:
            return 0
        valid = 0
        if root.val >= maxVal:
            if root.val > maxVal:
                maxVal = root.val
            valid = 1
        return self.dfs(root.left, maxVal) + self.dfs(root.right, maxVal) + valid
      
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)