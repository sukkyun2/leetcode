class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m,n = len(board), len(board[0])
        d = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        nei = []

        def out_of_index(i,j):
            return i<0 or j<0 or i>=m or j>=n

        for i in range(m):
            row = []
            for j in range(n):
                live = 0
                for x,y in d:
                    new_x, new_y = i+x, j+y
                    if out_of_index(new_x,new_y):
                        continue
                    if board[new_x][new_y]:
                        live += 1

                row.append(live)
            
            nei.append(row)         

        for i in range(m):
            for j in range(n):
                live = nei[i][j]
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 0
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 1

        

        