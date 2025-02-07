class Solution {
    public int eraseOverlapIntervals(int[][] times) {
        Arrays.sort(times, Comparator.comparingInt(it->it[1]));

        int last = times[0][1];
        int count = 1;

        for (int i = 1; i < times.length; i++) {
            if(last <= times[i][0]){
                last = times[i][1];
                count++;
            }
        }

        return times.length - count;
    }
}