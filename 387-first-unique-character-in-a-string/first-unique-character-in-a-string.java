import java.util.*;

class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> dict = new HashMap<>();

        for(int i=0;i<s.length();i++){
            Character c = Character.valueOf(s.charAt(i));
            dict.put(c, dict.getOrDefault(c,0)+1);
        }

        for(int i=0;i<s.length();i++){
            Character c = Character.valueOf(s.charAt(i));
            if(dict.get(c) == 1) return i;
        }
        
        return -1;
    }
}