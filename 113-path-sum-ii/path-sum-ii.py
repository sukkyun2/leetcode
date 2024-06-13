# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, path, rest):
            if not node:
                return
            
            rest -= node.val

            if not node.left and not node.right and rest == 0:
                ans.append(path + [node.val])
                return
            
            dfs(node.left, path + [node.val], rest)
            dfs(node.right, path + [node.val], rest)
            
        dfs(root, [], targetSum)
        return ans