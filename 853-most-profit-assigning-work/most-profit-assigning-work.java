import java.util.*;



class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int n = worker.length;
        int m = profit.length;
        int answer = 0;

        Arrays.sort(worker);

        List<Job> jobs = new ArrayList<>();
        for(int i=0;i<profit.length;i++){
            jobs.add(new Job(difficulty[i], profit[i]));
        }
        Collections.sort(jobs, Comparator.comparing(it->it.diff));

        int max = 0;
        for(int i=0, j=0;i<n;i++){
            while(j<m && worker[i] >= jobs.get(j).diff){
                max = Math.max(max, jobs.get(j).profit);
                j++;
            }
            answer += max;
        }


        return answer;
    }

    static class Job {
        int diff;
        int profit;

        public Job(int diff, int profit){
            this.diff = diff;
            this.profit = profit;
        }
    }
}