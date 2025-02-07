import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> answer = new ArrayList<>();
        Arrays.sort(intervals, (a,b)->Integer.compare(a[0],b[0]));
        
        answer.add(intervals[0]);

        for(int i=1;i<intervals.length;i++){
            int[] lastInterval = answer.get(answer.size()-1);

            if(intervals[i][0] <= lastInterval[1]){
                answer.set(answer.size()-1, new int[]{Math.min(lastInterval[0], intervals[i][0]), Math.max(lastInterval[1], intervals[i][1])});
            } else {
                answer.add(intervals[i]);
            }
        }

        int[][] result = new int[answer.size()][2];
        for(int i=0;i<answer.size();i++){
            result[i] = answer.get(i);
        }

        return result;
    }
}