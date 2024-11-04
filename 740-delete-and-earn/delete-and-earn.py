from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_value = max(counter.keys())
        min_value = min(counter.keys())
        
        dp = [0 for i in range(0, max_value+1)]

        dp[min_value] = min_value*counter[min_value]

        for n in range(2, max_value+1):
            dp[n] =  max(dp[n-1], dp[n-2] + n*counter[n])

        return dp[-1]