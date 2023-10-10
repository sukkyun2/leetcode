class Solution {
    public String longestCommonPrefix(String[] strs) {
        String firstString = strs[0];

        int i;
        for (i = 0; i < firstString.length(); i++) {
            char[] firstChars = firstString.toCharArray();

            boolean isCommonPrefix = false;
            int j;
            for (j = 0; j < strs.length; j++) {
                if(strs[j].toCharArray().length - 1 < i){ // if out of index
                    isCommonPrefix = false;
                    break;
                }
                
                isCommonPrefix = strs[j].toCharArray()[i] == firstChars[i];

                if (!isCommonPrefix) {
                    break;
                }
            }

            if (!isCommonPrefix) {
                break;
            }
        }
        
        return i == 0 ? "" : strs[0].substring(0, i);
    }
}