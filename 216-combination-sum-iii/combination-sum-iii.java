class Solution {
    private int K;
    private int N;
    private List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        K = k;
        N = n;

        backtracking(1,N, new ArrayList<>());

        return answer;
    }

    private void backtracking(int number, int rest, List<Integer> path){
        if(rest < 0) return;

        if(path.size() == K){
            if(rest == 0){
                answer.add(copy(path));
            }
            return;
        }

        for(int i=number;i<=9;i++){
            path.add(i);
            backtracking(i+1, rest-i, path);
            path.remove(path.size()-1);
        }
    }

    private List<Integer> copy(List<Integer> origin){
        return new ArrayList<>(origin);
    }
}