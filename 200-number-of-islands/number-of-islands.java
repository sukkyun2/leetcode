import java.util.*;

class Solution {
    static int M;
    static int N;

    public int numIslands(char[][] grid) {
        System.out.println(Arrays.deepToString(grid));
        int answer = 0;
        M = grid.length;
        N = grid[0].length;

        boolean[][] visited = new boolean[M][N];

        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(!visited[i][j] && grid[i][j] == '1'){
                    answer += 1;
                    bfs(i,j,visited,grid);
                }
            }
        }

        return answer;
    }

    private boolean outOfIndex(int i, int j){
        return i<0 || j<0 || i>=M || j>= N;
    }

    private void bfs(int i, int j, boolean[][] visited, char[][] grid){
        if(outOfIndex(i,j) || visited[i][j] || grid[i][j] == '0'){
            return;
        }

        visited[i][j] = true;

        bfs(i+1,j,visited,grid);
        bfs(i-1,j,visited,grid);
        bfs(i,j+1,visited,grid);
        bfs(i,j-1,visited,grid);
    }
}