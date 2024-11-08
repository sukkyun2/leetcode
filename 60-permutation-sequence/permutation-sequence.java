import java.util.*;

class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder();
        List<Integer> numbers = new ArrayList<>();
        int[] factorial = new int[10];
        factorial[0] = 1;
        k-=1;
        for(int i=1;i<factorial.length;i++){
            factorial[i] = factorial[i-1] * i;
            numbers.add(i);
        }

        for(int i=n;i>=1;i--){
            int index = k / factorial[i-1];
            sb.append(numbers.get(index));
            numbers.remove(index);
            k = k - index * factorial[i-1];
        }

        return sb.toString();
    }
}