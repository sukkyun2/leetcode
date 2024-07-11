class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(0,n):
            pattern = ''.join(map(str,[colors[i], colors[(i+1) % n], colors[(i+2) % n]]))
            if pattern in ['101','010']:
                ans += 1
                
        return ans
        