class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def out_of_index(x, y):
            return x < 0 or y < 0 or x >= m or y >= n

        def start_point():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j

        start = start_point()
        q = deque([start])
        visited[start[0]][start[1]] = True
        
        while q:
            i, j = q.popleft()
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_x, new_y = i + x, j + y
                if out_of_index(new_x, new_y) or grid[new_x][new_y] == 0:
                    ans += 1
                elif not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))
        return ans