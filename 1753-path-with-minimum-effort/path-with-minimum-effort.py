import heapq

class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        m,n = len(h), len(h[0])
        efforts = [[float('inf') for _ in range(n)] for _ in range(m)]
        efforts[0][0] = 0
        q = [(0,0,0)]

        def out_of_index(i,j):
            return i<0 or j<0 or i>=m or j>=n
        
        while q:
            e,i,j = heappop(q)

            if i == m-1 and j == n-1:
                return e

            for x,y in [(1,0),(-1,0),(0,-1),(0,1)]:
                new_x, new_y = i+x, j+y
                if out_of_index(new_x,new_y):
                    continue
                new_e = max(e, abs(h[i][j]-h[new_x][new_y]))
                if new_e < efforts[new_x][new_y]:
                    efforts[new_x][new_y] = new_e
                    heappush(q,(new_e,new_x,new_y))

        return -1