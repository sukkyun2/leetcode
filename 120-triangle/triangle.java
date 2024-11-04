import java.util.*;

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();

        for(int i=1;i<n;i++){
            List<Integer> row = triangle.get(i);
            List<Integer> prevRow = triangle.get(i-1);
            for(int j=0;j<row.size();j++){
                if(j==0){
                    row.set(j, row.get(j)+prevRow.get(j));
                } else if(j == row.size()-1){
                    row.set(j, row.get(j)+prevRow.get(j-1));
                } else {
                    row.set(j, row.get(j) + Math.min(prevRow.get(j-1), prevRow.get(j)));
                }
            }
        }

        return triangle.get(n-1).stream().mapToInt(it->it).min().orElse(0);
    }
}