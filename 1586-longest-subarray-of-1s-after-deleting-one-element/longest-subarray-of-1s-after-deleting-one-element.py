class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        one_cnt, zero_cnt = 0, 0
        front, rear = 0, 0
        n = len(nums)

        while n > rear:
            if nums[rear] == 1:
                one_cnt = one_cnt + 1
            elif nums[rear] == 0:
                zero_cnt = zero_cnt + 1

            while zero_cnt > 1:
                if nums[front] == 1:
                    one_cnt = one_cnt - 1
                elif nums[front] == 0:
                    zero_cnt = zero_cnt - 1
                
                front = front + 1
            
            ans = max(ans, one_cnt if zero_cnt > 0 else one_cnt - 1)

            rear = rear + 1

        return ans 
