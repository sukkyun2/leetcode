class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        ans = 0

        def out_of_index(i,j):
            return i>=m or j>=n or i<0 or j<0 

        def dfs(i,j,visited):
            visited.add((i,j))

            for x,y in directions:
                new_x, new_y = i+x, j+y
                if out_of_index(new_x,new_y) or grid[new_x][new_y] == "0" or (new_x,new_y) in visited:
                    continue
                
                dfs(new_x,new_y,visited)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j,visited)
                    ans+=1
        print(len(visited))
        return ans
        