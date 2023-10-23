# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ancestors = {}

    def find(self, x, root, ancestors = ancestors):
        LCA = None
        if root.val > x:
            LCA = self.find(x, root.left)
        elif root.val < x:
            LCA = self.find(x, root.right)
        if LCA:
            return LCA
        if root in ancestors:
            return root
        else:
            ancestors[root] = 1
            return None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find(p.val, root)
        return self.find(q.val, root)