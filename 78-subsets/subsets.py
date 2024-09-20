class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(index, path):
            ans.append(path)

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i+1, path[:])    
                path.pop()
        
        backtracking(0,[])

        return ans