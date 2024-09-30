class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g, reverse=True)
        s = sorted(s)
        ans = 0

        for gg in g:
            if not s:
                break
            
            if s[-1] >= gg:
                ans += 1
                s.pop()

        return ans