from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        costs = {i:float('inf') for i in range(1,n+1)}

        for u,v,w in times:
            adj[u].append((w,v)) # weight, other node

        costs[k] = 0
        q = [(0,k)]

        while q:
            cost, u = heappop(q)

            for w, v in adj[u]:
                new_cost = cost + w
                if new_cost < costs[v]:
                    costs[v] = new_cost
                    heappush(q,(new_cost,v))

        if float('inf') in costs.values():
            return -1

        return max(costs.values())    
            

