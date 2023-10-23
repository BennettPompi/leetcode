# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode], same = True) -> bool:
        if not same:
            return False
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            same = self.isSameTree(p.left, q.left, same)
            same = self.isSameTree(p.right, q.right, same)
        else:
            same = False
        return same