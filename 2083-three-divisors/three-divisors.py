class Solution:
    def isThree(self, n: int) -> bool:
        divisor = set()
        d = 1

        while d <= n:
            if n % d == 0:
                divisor.add(d)
                divisor.add(n//d)
            d+=1
        return len(divisor) == 3

        