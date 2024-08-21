from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        gap1, gap2 = c1 - c2, c2 - c1

        return all(v <= 3 for v in list(gap1.values()) + list(gap2.values()))