import java.util.*;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();

        int i=0;

        while(i < word1.length() && i < word2.length()){
            sb.append(word1.charAt(i));
            sb.append(word2.charAt(i));
            i++;
        }

        for(int j=i;j<word1.length();j++){
            sb.append(word1.charAt(j));
        }

        for(int j=i;j<word2.length();j++){
            sb.append(word2.charAt(j));
        }

        return sb.toString();
    }
}