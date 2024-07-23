class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        cost = [0] * n
        cost[start_node], hp = 1.0, [(-1.0, start_node)]
        adj = defaultdict(dict)

        for e, p in zip(edges, succProb):
            start, end = e
            adj[start][end] = p
            adj[end][start] = p

        while hp:
            prob, node = heapq.heappop(hp)

            if node == end_node:
                return -prob

            for u, p in adj[node].items():
                if -p * prob > cost[u]:
                    cost[u] = -p * prob
                    heapq.heappush(hp, (-cost[u], u))

        return 0.0