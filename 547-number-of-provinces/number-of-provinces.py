from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = defaultdict(list)
        n = len(isConnected)
        visited = set()
        cnt = 0

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    d[i].append(j)
        
        def dfs(i, visited):
            visited.add(i)

            for node in d[i]:
                if node not in visited:
                    dfs(node, visited)
        
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                cnt += 1

        return cnt