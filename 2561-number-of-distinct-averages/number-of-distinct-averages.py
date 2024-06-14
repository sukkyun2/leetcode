from collections import deque

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        q, s = deque(nums), set()

        for _ in range(len(nums)//2):
            minn, maxx = q.popleft(), q.pop()
            s.add((maxx+minn)/2)
        
        return len(s)
        