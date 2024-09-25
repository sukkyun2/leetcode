class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[float('inf') if i!=j else 0 for j in range(n)] for i in range(n)]
        neighbor = {i:0 for i in range(n)}
        
        for u,v,w in edges:
            d[u][v] = w
            d[v][u] = w
        
        for pivot in range(n):
            for i in range(n):
                for j in range(n):
                    new_distance = d[i][pivot] + d[pivot][j]
                    if d[i][j] > new_distance:
                        d[i][j] = new_distance
        
        for i in range(len(d)):
            count = 0 
            for j in d[i]:
                if j <= distanceThreshold:
                    count += 1
            neighbor[i] = count - 1
        
        min_value = min(neighbor.values())
        min_city = 0
        for city, count in neighbor.items():
            if count == min_value:
                min_city = city  

        return min_city