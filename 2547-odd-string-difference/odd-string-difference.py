from collections import Counter

class Solution:
    def oddString(self, words: List[str]) -> str:
        alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    
        n = len(words[0])
        diffs = []
        
        for word in words:
            diff = []
            for i in range(n-1):
                diff.append(alpha[word[i+1]] - alpha[word[i]])
            diffs.append(diff)

        for i, t in enumerate(zip(*diffs)):
            c = Counter(t)
            if 1 in c.values():
                for k, v in c.items():
                    if v == 1:
                        return words[list(t).index(k)]
                            
                    
                

        
        