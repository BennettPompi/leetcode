# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# just do DFS and add to array of arrays based on current layer. this solution massively overcomplicates the problem.
class Solution:
    def dfs(self, root, ans, layer=0):
        if not root:
            return
        if len(ans) <= layer:
            ans.append([root.val])
        else:
            ans[layer].append(root.val)
        self.dfs(root.left, ans, layer+1)
        self.dfs(root.right, ans, layer+1)
        return


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        self.dfs(root, answer)
        return answer