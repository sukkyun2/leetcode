class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        last=-1

        for i, c_num in enumerate(num):
            n = int(c_num)

            if n%2 == 0:
                continue
            
            last=i

        return num[:last+1]