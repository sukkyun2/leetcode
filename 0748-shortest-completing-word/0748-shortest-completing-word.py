from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = ''
        for c in licensePlate.lower():
            if c.isalpha():
                lp += c
        
        for word in sorted(words, key=len):
            counter = Counter(lp)
            for c in word:
                if counter[c]:
                    counter[c] -= 1
            print(counter)
            if all(v == 0 for v in counter.values()):
                return word