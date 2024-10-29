class Solution {
    public String mergeAlternately(String word1, String word2) {
        String ans = "";

        int i=0;

        while(i < word1.length() && i < word2.length()){
            ans += String.valueOf(word1.charAt(i));
            ans += String.valueOf(word2.charAt(i));
            i++;
        }

        for(int j=i;j<word1.length();j++){
            ans += String.valueOf(word1.charAt(j));
        }

        for(int j=i;j<word2.length();j++){
            ans += String.valueOf(word2.charAt(j));
        }

        return ans;
    }
}