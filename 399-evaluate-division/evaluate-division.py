class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def conv_adj():
            adj = defaultdict(list)
            for (start, end), value in zip(equations, values):
                adj[start].append((end, value))
                adj[end].append((start, 1 / value))
            return adj

        def dfs(end, curr, curr_val, visited):
            visited[curr] = True
            if curr == end:
                return curr_val

            for u, v in adj[curr]:
                if not visited[u]:
                    ans = dfs(end, u, v, visited)
                    if ans != -1.0:
                        return ans * curr_val

            return -1.0

        adj = conv_adj()
        ans = []
        for start, end in queries:
            if end not in adj.keys() or start not in adj.keys():
                ans.append(-1.0)
            else:
                ans.append(dfs(end, start, 1, defaultdict(bool)))

        return ans