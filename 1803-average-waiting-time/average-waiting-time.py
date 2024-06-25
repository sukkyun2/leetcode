class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_times = [customers[0][1]]
        end = sum(customers[0])

        for i in range(1,len(customers)):
            start, wait = customers[i] 
            wait_times.append(max(end - start,0) + wait)
            end = max(end, start) + wait 

        return sum(wait_times) / len(wait_times)

        