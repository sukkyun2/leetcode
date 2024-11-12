class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int front = 0, rear = numbers.length-1;

        while(front != rear){
            int twoSum = numbers[front] + numbers[rear];
            if(twoSum == target){
                return new int[]{front+1,rear+1};
            } else if(twoSum < target){
                front++;
            } else {
                rear--;
            }
        }

        return null;
    }
}