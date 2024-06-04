class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        front, rear = 0, 0
        sub_sum = nums[0]
        answer = float('inf')

        while rear < len(nums):
            if sub_sum < target:
                rear += 1
                if rear == len(nums): break

                sub_sum += nums[rear]  
            else:
                answer = min(answer,rear-front+1)
                sub_sum -= nums[front]
                front += 1
            
        return answer if answer != float('inf') else 0