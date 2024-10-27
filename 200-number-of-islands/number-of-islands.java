import java.util.*;

class Solution {
    private int m;
    private int n;
    private int[][] directions = new int[][]{
        {-1,0},
        {1,0},
        {0,1},
        {0,-1}
    };

    public int numIslands(char[][] grid) {
        m = grid.length;
        n = grid[0].length;
        int count = 0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] == '1'){
                    bfs(i,j,grid);
                    count+=1;
                }
            }
        }

        return count;
    }

    private void bfs(int i, int j, char[][] grid){
        Queue<int[]> q = new LinkedList<>(Arrays.asList(new int[]{i,j}));

        while(!q.isEmpty()){
            int[] e = q.poll();

            for(int[] d: directions){
                int x = e[0] + d[0];
                int y = e[1] + d[1];
                if(outOfIndex(x,y) || grid[x][y] == '0'){
                    continue;
                }

                grid[x][y] = '0';
                q.offer(new int[]{x,y});
            }
        }
    }

    private boolean outOfIndex(int i, int j){
        return i<0 || j<0 || i>=m || j>=n;
    }
}