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

            if ans <= rear-front+1:
                print(f"{rear} {front}")
                ans = rear-front+1


            rear += 1

        return ans
            
