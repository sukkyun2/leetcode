class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 1

            # if visited[i][j]:
            if grid[i][j] == -1:
                return 0

            grid[i][j] = -1
            
            return dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1) 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j)

        