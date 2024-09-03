class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            d, m = divmod(n, 2)
            if m != 0:
                return False

            n = d

        return True