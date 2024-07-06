from collections import deque

class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        m,n = len(h), len(h[0])
        efforts = {(i,j):float('inf') for j in range(n) for i in range(m)}
        efforts[(0,0)] = 0
        q = deque([(0,0)])

        def out_of_index(i,j):
            return i < 0 or i >= m or j < 0 or j >= n

        while q:
            i, j = q.popleft()

            # if i == m-1 and j == n-1:
            #     print(efforts)
            #     return efforts[(i,j)]
            
            for x, y in [(1,0),(-1,0),(0,-1),(0,1)]:
                new_x, new_y = i+x, j+y
                if out_of_index(new_x, new_y):
                    continue
                
                effort = max(efforts[(i,j)], abs(h[i][j]-h[new_x][new_y]))
                if effort < efforts[(new_x,new_y)]:
                    efforts[(new_x,new_y)] = effort
                    q.append((new_x,new_y))


        return efforts[(m-1,n-1)]