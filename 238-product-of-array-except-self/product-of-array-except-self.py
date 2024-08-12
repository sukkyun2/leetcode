class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        front, rear = 1, 1
        ans = [1] * n

        for i in range(len(nums)):
            ans[i] = ans[i] * front
            ans[n-1-i] = ans[n-1-i] * rear

            front = front * nums[i]
            rear = rear * nums[n-1-i]
        
        return ans
        