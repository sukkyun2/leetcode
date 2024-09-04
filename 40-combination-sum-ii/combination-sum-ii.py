class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        candidates.sort()

        def backtracking(i, rest, path):
            if rest < 0:
                return
            
            if rest == 0:
                self.ans.add(tuple(path))
                return

            for ii, j in enumerate(candidates[i:]):
                if ii > 0 and j == candidates[ii-1]:
                    continue
                backtracking(i+ii+1, rest - j, path[:] + [j]) 
        
        backtracking(0, target, [])

        return set(self.ans)