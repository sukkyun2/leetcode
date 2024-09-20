class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(index, path): 
            ans.add(tuple(sorted(path)))

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i+1, path[:])
                path.pop()

        ans = set()
        backtracking(0,[])

        return ans

        