import java.util.*;

class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        Set<Integer> answer = new HashSet<>();

        for(int j=0;j<nums.length;j++){
            if(nums[j] != key){
                continue;
            }

            int start = Math.max(0, j-k);
            int end = Math.min(nums.length-1, j+k);
            
            for(int i=start;i<=end;i++){
                answer.add(i);
            }
        }
        
        return answer.stream().sorted().collect(Collectors.toList());
        // return answer;
    }
}