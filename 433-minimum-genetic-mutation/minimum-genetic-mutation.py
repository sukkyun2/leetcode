class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def diff(s1,s2):
            cnt = 0
            for c1, c2 in zip(s1,s2):
                if c1 != c2:
                    cnt+=1
            return cnt

        def dfs(gene, visited, ans):
            visited.add(gene)

            if gene == endGene:
                ans[0] = min(ans[0], len(visited)-1)
                return

            min_count = float('inf')
            for g_bank in bank:
                if g_bank not in visited and diff(gene, g_bank) == 1:
                    dfs(g_bank, visited.copy(), ans) 
                    
            return -1

        visited = set()
        ans = [float('inf')]
        dfs(startGene, visited, ans)
        
        return ans[0] if ans[0] != float('inf') else -1
            

