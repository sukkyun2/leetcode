class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        cnt = 0 

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            parent[root_a] = root_b

            return root_a != root_b
        
        for i in range(n):
            for j in range(i+1,n):    
                if isConnected[i][j] and union(i,j):
                    cnt += 1
        
        return n - cnt