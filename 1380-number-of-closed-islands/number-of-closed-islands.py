class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        cnt = 0

        def out_of_index(i,j):
            return i<0 or j<0 or i>=m or j>=n

        def dfs(i,j):
            if out_of_index(i,j):
                return False
            if grid[i][j] or (i,j) in visited:
                return True

            visited.add((i,j))
            
            left = dfs(i-1, j)
            right = dfs(i+1, j)
            top = dfs(i, j-1)
            bottom = dfs(i, j+1)

            return left and right and top and bottom    

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in visited and dfs(i,j):
                    print(f"{i} {j}")
                    cnt += 1 

        return cnt
