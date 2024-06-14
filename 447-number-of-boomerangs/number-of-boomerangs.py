from collections import Counter

class Solution:
    def numberOfBoomerangs(self, p: List[List[int]]) -> int:
        ans = 0
        def get_distance(a,b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2
        
        for i in range(len(p)):
            counter = Counter([get_distance(p[i], p[j]) for j in range(len(p))])

            for i in counter.values():
                if i >= 2:
                     ans += i * (i-1)

        return ans
        