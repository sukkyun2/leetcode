class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        for e in pushed:
            stack.append(e)
            while stack and popped and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
        
        for _ in range(len(stack)):
            if stack.pop() != popped.pop(0):
                return False
        
        return True
