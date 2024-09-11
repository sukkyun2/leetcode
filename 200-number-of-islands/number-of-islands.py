class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        ans = 0 

        def out_of_index(i,j):
            return i<0 or j<0 or i>=m or j>=n

        def dfs(i,j,visited):
            stack = [(i,j)]
            
            while stack:
                ii, jj = stack.pop()
                visited.add((ii,jj))
                
                for x,y in directions:
                    new_x,new_y = ii+x, jj+y
                    if out_of_index(new_x,new_y) or (new_x,new_y) in visited or grid[new_x][new_y] == "0":
                        continue
                    stack.append((new_x,new_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j,visited)
                    ans+=1

        return ans