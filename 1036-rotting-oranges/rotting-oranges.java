import java.util.*;

class Solution {
    private int m;
    private int n;
    private List<int[]> directions = Arrays.asList(
        new int[]{1,0},
        new int[]{0,1},
        new int[]{-1,0},
        new int[]{0,-1}
    ); 

    public int orangesRotting(int[][] grid) {
        m = grid.length;
        n = grid[0].length;

        List<int[]> start = new ArrayList<>();
        int frashCount = 0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] == 2){
                    start.add(new int[]{i,j});
                } else if(grid[i][j] == 1){
                    frashCount++;
                }
            }
        }

        return bfs(start, grid, frashCount);
    }

    private int bfs(List<int[]> start, int[][] grid, int frashCount){
        int count = 0;
        Queue<int[]> q = new LinkedList<>(start);

        while(!q.isEmpty() && frashCount > 0){
            int size = q.size();
            for(int i=0;i<size;i++){
                int[] e = q.poll();

                for(int[] d: directions){
                    int x = e[0] + d[0];
                    int y = e[1] + d[1];

                    if(outOfIndex(x,y) || grid[x][y] != 1){
                        continue;
                    }

                    grid[x][y] = 2;
                    frashCount--;
                    q.offer(new int[]{x,y});
                }
            }
            count++;
        }
        System.out.print(frashCount);

        return frashCount == 0 ? count : -1;
    }

    private boolean outOfIndex(int i, int j){
        return i<0 || j<0 || i>=m || j>=n;
    }
}