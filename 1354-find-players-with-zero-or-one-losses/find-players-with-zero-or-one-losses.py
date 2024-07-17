class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = dict()
        ans = [[],[]]

        for w, l in matches:
            if not d.get(w):
                d[w] = 0
            
            if not d.get(l):
                d[l] = 1
            else:
                d[l] += 1

        for p in sorted(d.keys()):
            l = d[p]
            if l == 0:
                ans[0].append(p)
            elif l == 1:
                ans[1].append(p)
        
        return ans
        