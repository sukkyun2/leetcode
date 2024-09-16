class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        max_number = 9

        def backtracking(idx,path,rest):            
            if rest<0 or len(path)>k:
                return
            if rest==0 and len(path)==k:
                ans.append(path)
                return

            for i in range(idx,max_number+1):
                path.append(i)
                backtracking(i+1, path[:], rest - i)
                path.pop()
            
        backtracking(1,[],n)

        return ans