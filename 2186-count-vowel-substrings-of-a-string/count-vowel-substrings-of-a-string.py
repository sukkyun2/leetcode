class Solution:
    def countVowelSubstrings(self, w: str) -> int:
        l = len(w)
        ans = 0
        vowels = set(['a','e','i','o','u'])

        for i in range(l):
            if w[i] not in vowels:
                continue
            
            cur = set()
            for j in range(i,l):
                if w[j] not in vowels:
                    break
                cur.add(w[j])
                if len(cur) == len(vowels):
                    ans += 1

        return ans