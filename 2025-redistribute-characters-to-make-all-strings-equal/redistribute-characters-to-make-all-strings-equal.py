from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        n = len(words)
        
        for word in words:
            c = Counter(word)
            counter = counter + c
        
        return all(v % n == 0 for v in counter.values())
        