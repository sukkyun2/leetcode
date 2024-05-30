class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans, words = [], text.split()
        for i in range(2, len(words)):
            f, s = words[i-2], words[i-1]
            if f == first and s == second:
                ans.append(words[i])

        return ans
            
        