# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft: bool=False) -> int:
        if not root:
            return 0
        
        def isLeaf(node: TreeNode):
            return not node.left and not node.right
        
        curr = root.val if isLeft and  isLeaf(root) else 0
        return curr + self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
        
            