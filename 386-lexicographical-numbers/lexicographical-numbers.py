class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(num_str):
            num = int(num_str)
            if num > n:
                return
            ans.append(num)

            for i in range(10):
                dfs(num_str + str(i))

        for i in range(1,10):
            dfs(str(i))

        return ans

        