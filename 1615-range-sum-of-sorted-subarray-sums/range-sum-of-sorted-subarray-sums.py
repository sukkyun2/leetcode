class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(1,n+1):
            for j in range(n):
                if j+i > n:
                    continue
                ans.append(sum(nums[j:j+i]))

        return sum(sorted(ans)[left-1:right]) % (10**9+7)
