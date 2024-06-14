class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        cal = sorted(map(lambda cost: (cost[0]-cost[1],cost), costs), key=lambda c: abs(c[0]), reverse=True)
        
        A, B = [], []

        i = 0
        while i < len(cal) and len(A) < n and len(B) < n:
            diff, cost = cal[i]
            if diff < 0:
                A.append(cost[0])
            else:
                B.append(cost[1])
            i+=1
        
        while len(B) < n:
            diff, cost = cal[i]
            B.append(cost[1])
            i+=1
        
        while len(A) < n:
            diff, cost = cal[i]
            A.append(cost[0])
            i+=1            
                
        return sum(A) + sum(B)