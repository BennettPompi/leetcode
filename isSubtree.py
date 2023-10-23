# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSame(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return (self.isSame(r.left, s.left) and self.isSame(r.right, s.right))
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    """
    def checkSubTree(root, subRoot):
        if not root or not subRoot:
            if isinstance(root, TreeNode) == isinstance(subRoot, TreeNode):
                return True
            else:
                return False
        if Solution.checkSubTree(root.left, subRoot.left) and Solution.checkSubTree(root.right, subRoot.right):
            return root.val == subRoot.val
        else:
            return False
    def searchForSubRoot(root, subRoot, found):
        if not root:
            return False
        if root.val == subRoot.val and not found:
            found = Solution.checkSubTree(root, subRoot)
        if not found:
            lfound = Solution.searchForSubRoot(root.left, subRoot, found)
            rfound = Solution.searchForSubRoot(root.right, subRoot, found)
            found = (lfound or rfound)
        return found
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return Solution.searchForSubRoot(root, subRoot, False)"""