# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return not node.left and not node.right
        def conv_number(b_number):
            num = 0
            p = 0
            for c in b_number[::-1]:
                num += int(c) * 2**p
                p+=1
            return num

        b_numbers = []
        stack = [(root, '')]
        while stack:
            node, b_str = stack.pop()
            b_str += str(node.val)

            if isLeaf(node):
                b_numbers.append(b_str)
            
            if node.left:
                stack.append((node.left, b_str))
            if node.right:
                stack.append((node.right, b_str))
        
        print(b_numbers)
        return sum(conv_number(num) for num in b_numbers)
            

        