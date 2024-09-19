from itertools import combinations 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        for i in range(0, n+1):
            ans = ans + list(combinations(nums, i))

        return ans