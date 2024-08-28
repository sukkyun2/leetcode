# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        def is_leaf(node):
            return not node.left and not node.right

        def dfs(node, paths):
            paths += str(node.val)

            if is_leaf(node):
                ans.append(paths)
                return
            
            if node.left:
                dfs(node.left, paths + '')
            if node.right:
                dfs(node.right, paths + '')
            
        dfs(root, "")

        return sum(map(int, ans))
            
            
