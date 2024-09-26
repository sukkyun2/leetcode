class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        people_max = len(costs)//2
        ans = 0
        count_a, count_b = 0,0
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)
        print(costs)

        i=0
        while i < len(costs) and count_a < people_max and count_b < people_max:
            a,b = costs[i]
            if a < b:
                print(a)
                count_a += 1
                ans += a
            else:
                print(b)
                count_b += 1
                ans += b
            i+=1 
        
        while count_a != people_max:
            count_a += 1
            ans += costs[i][0]
            i+=1 
        while count_b != people_max:
            count_b += 1
            ans += costs[i][1]
            i+=1

        return ans
        