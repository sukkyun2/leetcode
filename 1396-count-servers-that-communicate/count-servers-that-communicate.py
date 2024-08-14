from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        adj_x, adj_y = defaultdict(list), defaultdict(list)
        target = []
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    target.append((x,y))
                    adj_x[x].append(y)
                    adj_y[y].append(x)
        
        for x, y in target:
            if len(adj_x[x]) >= 2 or len(adj_y[y]) >= 2:
                ans = ans+1

        return ans

        