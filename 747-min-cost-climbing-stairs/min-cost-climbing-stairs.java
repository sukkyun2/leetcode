import java.util.*;

class Solution {
    private int[] memo;

    public int minCostClimbingStairs(int[] cost) {
        int N = cost.length;
        memo = new int[N];
        memo[0] = cost[0];
        memo[1] = cost[1];

        for(int i=2;i<N;i++){
            memo[i] = cost[i] + Math.min(memo[i-1], memo[i-2]);
        }

        return Math.min(memo[N-2], memo[N-1]);
    }
}