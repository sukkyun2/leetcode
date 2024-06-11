class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        max_len = max(len(word) for word in words)
        
        for i, w in enumerate(words):
            if len(w) < max_len:
                words[i] = words[i] + ' ' * (max_len - len(w))
            
        return [''.join(list(t)).rstrip() for t in zip(*words)]

        
        