from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def convert_adj():
            adj = defaultdict(list)
            for s,e in edges:
                adj[s].append(e)
                adj[e].append(s)
            
            return adj
        
        adj = convert_adj()
        rest = set(restricted)

        def dfs(v, visited):
            if v in visited or v in rest:
                return 0
            
            visited.add(v)
            
            return 1 + sum(dfs(u, visited) for u in adj[v])
        
        return dfs(0, set())   
        