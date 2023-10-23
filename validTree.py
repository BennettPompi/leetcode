# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sys import maxsize
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minValue = -maxsize, maxValue = maxsize) -> bool:
        return True if not root else(root.val > minValue and root.val < maxValue and 
                                     self.isValidBST(root.left, minValue, root.val) and 
                                     self.isValidBST(root.right, root.val, maxValue))
        """
        if not root:
            return True
        valid = True
        if root.left: 
            if root.left.val < root.val and root.left.val > minValue:
                valid = self.isValidBST(root.left, minValue, maxValue = min(maxValue, root.val))
            else:
                valid = False
        if valid and root.right:
            if root.right.val > root.val and root.right.val < maxValue:
                valid = self.isValidBST(root.right,minValue=max(minValue, root.val), maxValue = maxValue)
            else:
                valid = False
        return valid
        """