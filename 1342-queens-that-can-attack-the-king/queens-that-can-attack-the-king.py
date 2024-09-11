class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        m, n = 8,8
        queen_set = set(map(tuple,queens))
        directions = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

        def out_of_index(i,j):
            return 8<=i or 8<=j or i<0 or j<0

        def search_queens(direaction, attackable_queens):
            king_x, king_y = king.copy()
            while not out_of_index(king_x, king_y):
                print(f"{king_x} {king_y}")
                king_x, king_y = king_x + direaction[0], king_y + direaction[1]
                if (king_x, king_y) in queen_set:
                    attackable_queens.add((king_x, king_y))
                    return

        for i in range(m):
            for j in range(n):
                if [i,j] == king:
                    attackable_queens = set()

                    for d in directions:
                        search_queens(d, attackable_queens) 

                    return attackable_queens