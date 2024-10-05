class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        memo = [0] * (n+1)
        memo[0], memo[1] = 0,1

        for i in range(n-1):
            memo[i+2] = memo[i+1] + memo[i]

        return memo[n] 
        