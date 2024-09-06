class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        filtered = ''.join([c for c in s.lower() if c.isnumeric() or c.islower()])
        return filtered == filtered[::-1]


        