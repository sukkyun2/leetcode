class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];

        Arrays.fill(dp, 1); //0일수는 없음 최소 1

        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(nums[i] > nums[j]){
                    dp[i] = Math.max(dp[j]+1, dp[i]);
                }
            }
        }

        return Arrays.stream(dp).max().orElse(1); //마지막이 무조건 최대라는 보장이 없음
    }
}