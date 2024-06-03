class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def resolve(a,b,op):
            if token == '+':
                return a+b
            elif token == '-':
                return a-b
            elif token == '*':
                return a*b
            elif token == '/':
                return int(a/b)

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b, a = stack.pop(), stack.pop()
                stack.append(resolve(a,b,token))
            else: # number
                stack.append(int(token))
        return stack[-1]