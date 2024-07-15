import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cost = [[float('inf') for _ in range(n)] for _ in range(m)]
        cost[0][0] = 1
        q = [(0,0,0)]

        def out_of_index(i,j):
            return i < 0 or j < 0 or i >= m or j >= n

        while q:
            w, i, j = heappop(q)

            if i == m-1 and j == n-1:
                return w

            for d_x, d_y in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_x, new_y = i+d_x, j+d_y
                if out_of_index(new_x, new_y):
                    continue

                new_w = w + grid[new_x][new_y]
                if new_w < cost[new_x][new_y]:
                    cost[new_x][new_y] = new_w
                    heappush(q, (new_w, new_x, new_y)) 

        return -1
