class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        d = [(1,0),(0,1),(-1,0),(0,-1)]

        def out_of_index(i,j):
            return i<0 or j<0 or i>=m or j>=n

        def dfs(i,j):
            visited.add((i,j))

            for x,y in d:
                ii,jj = i+x, j+y
                if out_of_index(ii,jj) or (ii,jj) in visited or grid[ii][jj] == 0:
                    continue
                dfs(ii,jj)
        
        def count_bridge():
            q = deque(visited)
            count = 0
            
            while q:
                for _ in range(len(q)):
                    i,j = q.popleft()
                    for x,y in d:
                        ii,jj = i+x, j+y
                        if out_of_index(ii,jj) or (ii,jj) in visited:
                            continue
                        if grid[ii][jj]:
                            print(f"{ii} {jj}")
                            return count
                        visited.add((ii,jj))
                        q.append((ii,jj))
                count += 1

        def search_first_land():
            for i in range(m):
                for j in range(n):
                    if grid[i][j]:
                        dfs(i,j)
                        return
        
        search_first_land()
        return count_bridge()
                
            
        