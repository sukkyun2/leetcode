class Solution {
    public boolean isPalindrome(int x) {
        int number = x;

        if(number < 0 || (number % 10 == 0 && number != 0)) return false;

        int reversed = 0;
        while(number != 0){
            reversed = reversed * 10 + number % 10;

            number /= 10;
        }

        return x == reversed;
    }
}