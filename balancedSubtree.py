class Solution:
    #faster solution is to memoize sub-heights using dict with nodes as keys
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lbalanced = self.isBalanced(root.left)
        rbalanced = self.isBalanced(root.right)
        return abs(self.depth(root.left) - self.depth(root.right) > 1) and (lbalanced and rbalanced)
        