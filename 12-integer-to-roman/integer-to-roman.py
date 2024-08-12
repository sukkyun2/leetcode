class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        for n, roman in d.items():
            if num >= n:
                q, r = divmod(num, n)
                ans = ans + q * roman
                num = r
        return ans 
            