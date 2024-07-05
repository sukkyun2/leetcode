class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        elif x == 2:
            return 1

        for i in range(1,x):
            double_i = i**2
            if double_i == x:
                return i
            elif double_i > x:
                return i-1
        