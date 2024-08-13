class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        front, rear = 0, 0
        n = len(nums)

        while n > rear:
            if nums[rear] == 0:
                k = k-1
            
            while k < 0:
                if nums[front] == 0:
                    k = k+1
                front = front + 1

            gap = rear-front+1
            ans = max(ans, gap)

            rear += 1

        return ans
            
