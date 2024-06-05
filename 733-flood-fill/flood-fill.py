from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])

        def outOfIndex(x,y):
            return x < 0 or y < 0 or x >= m or y >= n

        def bfs():
            og = image[sr][sc]
            if og == color: return

            q = deque([(sr,sc)])
            image[sr][sc] = color 

            while q:
                i, j = q.popleft()
                
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_x, new_y = i + x, j + y
                    if not outOfIndex(new_x, new_y) and image[new_x][new_y] == og:
                        image[new_x][new_y] = color
                        q.append((new_x, new_y))
    
        bfs()

        return image

        

