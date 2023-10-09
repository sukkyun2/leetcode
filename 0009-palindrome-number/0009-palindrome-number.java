class Solution {
    public boolean isPalindrome(int x) {
        String str = String.valueOf(x);
        String reversedStr = new StringBuilder(str).reverse().toString();

        return str.equals(reversedStr);
    }
}