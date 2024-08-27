class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        i = 1

        for e in arr:
            while i != e:
                cnt += 1

                if cnt == k:
                    return i
                    
                i += 1



            i+=1
        
        return arr[-1] + (k-cnt)