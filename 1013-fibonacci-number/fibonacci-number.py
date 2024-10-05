class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        memo = [-1] * (n+1)
        memo[0], memo[1] = 0,1 

        def dp(i):
            if memo[i] == -1:
                memo[i] = dp(i-1) + dp(i-2)
                return memo[i]
            else:
                return memo[i]

        return dp(n)
        