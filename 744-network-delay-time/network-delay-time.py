import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def get_adj():
            adj = defaultdict(list)
            for u,v,w in times:
                adj[u].append((v,w))
            
            return adj
        
        ans = 0
        adj = get_adj()
        cost = {i: float('inf') for i in range(1,n+1)}

        cost[k] = 0
        q = [(0,k)]

        while q:
            cur_w, u = heappop(q)

            # if not adj[u] or any(i != float('inf') for i in cost):
            #    ans = max(ans, cur_w) 

            for v,w in adj[u]:
                next_w = cur_w + w
                
                if next_w < cost[v]:
                    cost[v] = next_w
                    heappush(q,(cur_w+w,v))
        
        if float('inf') in cost.values():
            return -1

        return max(cost.values())
        