from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_1, dic_2 = defaultdict(str), defaultdict(str)
        
        for c1, c2 in zip(s,t):
            if not dic_1[c1] and not dic_2[c2]:
                dic_1[c1] = c2
                dic_2[c2] = c1
            elif dic_1[c1] != c2 or dic_2[c2] != c1:
                return False 

        return True
