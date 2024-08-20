class Solution:
    def minimumMoves(self, s: str) -> int:
        i, n = 0, len(s)
        ans = 0
        while i < n:
            if s[i] == 'O':
                i = i+1
                continue
            
            ans = ans+1
            i = i+3
        
        return ans