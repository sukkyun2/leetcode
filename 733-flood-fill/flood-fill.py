from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def outOfIndex(x,y):
            return x < 0 or y < 0 or x >= m or y >= n

        def bfs():
            og = image[sr][sc]
            q = deque([(sr,sc)])
            visited[sr][sc] = True
            image[sr][sc] = color 

            while q:
                i, j = q.popleft()
                
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_x, new_y = i + x, j + y
                    if not outOfIndex(new_x, new_y) and not visited[new_x][new_y] and image[new_x][new_y] == og:
                        visited[new_x][new_y] = True
                        image[new_x][new_y] = color
                        q.append((new_x, new_y))
    
        bfs()

        return image

        

