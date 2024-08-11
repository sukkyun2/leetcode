from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        def hash(s: str):
            return ''.join(sorted(s))

        for s in strs:
            d[hash(s)].append(s)

        return d.values()