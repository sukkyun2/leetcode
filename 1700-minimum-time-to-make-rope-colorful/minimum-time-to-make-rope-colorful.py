import pprint

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        stack = []
        for c, t in zip(colors, neededTime):
            if not stack:
                stack.append((c,t))
                continue
            
            prev_color, prev_time = stack[-1]
            if prev_color == c:
                if prev_time > t: # t 제거
                    answer += t
                else: # prev 제거
                    answer += prev_time
                    stack.pop()
                    stack.append((c,t))
            else:
                stack.append((c,t))
        return answer
        