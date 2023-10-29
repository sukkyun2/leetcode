class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ranges = new ArrayList<>();

        int front = 0;
        int rear = 0;
        while (rear <= nums.length - 1) {
            if(rear == nums.length - 1){
                String range = rear == front ? "" + nums[rear] : nums[front] + "->" + nums[rear];
                ranges.add(range);
                break;
            }

            //FIXME outofindex가 뜨네 체크할 때 i를 기준으로 i-1이런식으로 체크해야하나?
            if(nums[rear] + 1 == nums[rear+1]){
                rear++;
            } else if(rear == front){
                ranges.add("" + nums[rear]);

                front = ++rear;
            } else {
                String range = nums[front] + "->" + nums[rear];
                ranges.add(range);

                front = ++rear;
            }
        }

        return ranges;
    }
}