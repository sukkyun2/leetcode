from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt_s, cnt_t = Counter(s), Counter(t)
        diff = cnt_t - cnt_s
        return ''.join(diff.keys())