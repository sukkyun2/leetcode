class Solution:
    def countArrangement(self, n: int) -> int:
        path = []
        self.ans = 0

        def is_divisible(index, value):
            return index % value == 0 or value % index == 0 

        def backtracking(path):
            if len(path) == n:
                self.ans += 1
                return
            
            for i in range(1, n+1):
                if i in path or not is_divisible(len(path)+1, i):
                    continue

                path.append(i)
                backtracking(path[:])
                path.pop()

        backtracking(path)

        return self.ans