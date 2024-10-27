import java.util.*;

class Solution {
    private int N;
    public int findCircleNum(int[][] isConnected) {
        int count = 0;
        Map<Integer, List<Integer>> adj = new HashMap<>();

        int N = isConnected.length;
        int m = isConnected.length;
        int n = isConnected[0].length;
        Set<Integer> visited = new HashSet<>();

        for(int i=0;i<m;i++){
            adj.put(i, new ArrayList<>());
        }

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(i==j) continue;

                if(isConnected[i][j] == 1){
                    adj.get(i).add(j);
                }
            }
        }

        for(int i=0;i<m;i++){
            if(!visited.contains(i)){
                bfs(i,adj,visited);
                count+=1;
            }
        }
        
        return count;
    }

    private void bfs(int i, Map<Integer, List<Integer>> adj, Set<Integer> visited){
        visited.add(i);

        for(Integer v: adj.get(i)){
            if(!visited.contains(v)){
                bfs(v,adj,visited);
            }
        }
    }
}