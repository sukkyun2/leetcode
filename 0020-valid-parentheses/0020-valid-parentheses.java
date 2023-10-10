class Solution {
    private static Map<Character,Character> dictionary = Map.of('(',')','{','}','[',']');

    public boolean isValid(String s) {
        Stack<Character> characters = new Stack<>();
        boolean isValid = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if(dictionary.containsKey(c)){
                characters.push(c);
                isValid = false;
            } else {
                if(characters.empty()){
                    return false;
                }

                Character pop = characters.pop();
                isValid = dictionary.get(pop) == c;

                if(!isValid) {
                    break;
                }
            }
        }

        return characters.empty() && isValid;
    }
}