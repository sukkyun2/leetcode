class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        front, rear, cnt = 0, len(nums)-1, 0
        nums = sorted(nums)

        while front < rear:
            s = nums[front] + nums[rear]

            if s < k:
                front += 1
            elif s > k:
                rear -= 1
            else: # s == k
                cnt += 1
                front += 1
                rear -= 1

        return cnt