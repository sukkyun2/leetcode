class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])

        def out_of_index(i,j):
            return i<0 or j<0 or i>=m or j>=n

        def dfs(i,j, visited):
            if out_of_index(i,j):
                return False
            if board[i][j] == 'X' or (i,j) in visited:
                return True

            visited.add((i,j))

            left = dfs(i-1,j, visited)
            right = dfs(i+1,j, visited)
            top = dfs(i,j-1, visited)
            bottom = dfs(i,j+1, visited)

            return left and right and top and bottom
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    visited = set()
                    if dfs(i,j, visited):
                        for x,y in visited:
                            board[x][y] = 'X'

        
        