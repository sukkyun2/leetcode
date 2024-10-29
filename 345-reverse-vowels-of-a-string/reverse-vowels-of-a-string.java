import java.util.*;

class Solution {
    public String reverseVowels(String s) {
        int front = 0;
        int rear = s.length() - 1;
        StringBuilder sb = new StringBuilder(s);
        
        while(front < rear){
            if(!isVowel(sb.charAt(front))){
                front+=1;
            } else if(!isVowel(sb.charAt(rear))){
                rear-=1;
            } else {
                char temp = sb.charAt(front);
                sb.setCharAt(front,sb.charAt(rear));
                sb.setCharAt(rear,temp);
                front +=1;
                rear -=1;
            }
        }

        return sb.toString();
    }

    private boolean isVowel(char c){
        char lower = Character.toLowerCase(c);
        return lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u';
    }
}