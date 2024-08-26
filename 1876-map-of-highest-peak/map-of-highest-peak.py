from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[0] * n for _ in range(m)]

        q = deque([(i, j) for j in range(n) for i in range(m) if isWater[i][j] == 1])
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        level = 1

        def out_of_index(i, j):
            return m <= i or n <= j or i < 0 or j < 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in d:
                    new_x, new_y = i + x, j + y

                    if (
                        out_of_index(new_x, new_y)
                        or (new_x, new_y) in visited
                        or isWater[new_x][new_y] == 1
                    ):
                        continue

                    visited.add((new_x, new_y))
                    ans[new_x][new_y] = level
                    q.append((new_x, new_y))
            level += 1

        return ans
