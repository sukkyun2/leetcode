class Solution {
    public int lengthOfLastWord(String s) {
        int start = s.length() - 1;
        while (start >= 0 && s.charAt(start) == ' '){
            start--;
        }
        
        int end = start - 1;
        while (end >= 0 && s.charAt(end) != ' '){
            end--;
        }

        return start - end;
    }
}