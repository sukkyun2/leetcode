class Solution:
    def bestClosingTime(self, cs: str) -> int:
        cost = cs.count('Y')
        min_idx, min_cost = 0, cost

        for i in range(1,len(cs)+1):
            cost = cost - 1 if cs[i-1] == 'Y' else cost + 1
            
            if min_cost > cost:
                min_cost, min_idx = cost, i

        return min_idx
                
        
