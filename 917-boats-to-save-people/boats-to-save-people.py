class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        ans, front, rear = 0, 0, len(p) - 1

        while front < rear:
            tot = p[front] + p[rear]
            if tot > limit:
                rear -= 1
            elif tot <= limit:
                front += 1
                rear -= 1
            
            ans += 1   

        return ans + (front == rear)
        
        