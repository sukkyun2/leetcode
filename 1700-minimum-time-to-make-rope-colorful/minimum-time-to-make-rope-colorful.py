import pprint

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        prev, prev_max = '', 0
        for c, t in zip(colors, neededTime):
            if prev != c:
                prev, prev_max = c, t
            else: # prev == c
                answer += min(prev_max, t)
                prev_max = max(prev_max, t)

        return answer
        