import java.util.*;

class Solution {
    int n;
    public int minFallingPathSum(int[][] matrix) {
        n = matrix.length;

        for(int i=1;i<n;i++){
            for(int j=0;j<n;j++){
                matrix[i][j] = matrix[i][j] + Math.min(getValue(i-1,j-1,matrix), Math.min(getValue(i-1,j,matrix), getValue(i-1,j+1,matrix)));
            }
        }

        return Arrays.stream(matrix[n-1]).min().orElse(0);
    }

    private int getValue(int i, int j, int[][] matrix){
        return outOfIndex(i,j) ? Integer.MAX_VALUE : matrix[i][j];
    }

    private boolean outOfIndex(int i, int j){
        return i<0 || j<0 || i>=n || j>=n; 
    }
}