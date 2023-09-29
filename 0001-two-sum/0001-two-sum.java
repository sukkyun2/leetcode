class Solution {
    public int[] twoSum(int[] nums, int target) {
        int firstIndex = 0;
        int secondIndex = 0;

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int twoSum = nums[i] + nums[j];

                if (twoSum == target) {
                    firstIndex = i;
                    secondIndex = j;
                }
            }
        }

        return new int[]{firstIndex, secondIndex};
    }
}