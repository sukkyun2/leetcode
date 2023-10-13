class Solution {
    public static int[] memory = new int[46];

    public int climbStairs(int n) {
        if (n == 1 || n == 2) {
            return n;
        }

        if (memory[n] == 0) {
            memory[n] = climbStairs(n - 1) + climbStairs(n - 2);
        }

        return memory[n];
    }
}