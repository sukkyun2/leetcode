class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if(str1.length() < str2.length()){
            return gcdOfStrings(str2, str1);
        } 
        
        if(str2.isEmpty()){
            return str1;
        }

        int n = str2.length();
        if(str1.substring(0,n).equals(str2)){ //str1.startsWith(str2)
            return gcdOfStrings(str2, str1.substring(n));
        }

        return "";
    }
}