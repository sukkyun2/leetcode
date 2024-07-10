class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ans = 0
        vowels = set(['a','e','o','u','i'])
        v, c = 0, 0  
        for i,ch in enumerate(s):
            if ch in vowels:
                v += 1
            else:
                c += 1
            
            front = 0
            vv = v
            cc = c
            while vv >= 0 and cc >= 0 and front <= i:
                if vv == cc and (vv*cc) % k == 0:
                    ans +=1
                
                if s[front] in vowels:
                    vv -= 1
                else:
                    cc -= 1

                front += 1
        
        return ans