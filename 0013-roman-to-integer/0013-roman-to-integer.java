class Solution {
    private static Map<Character, Integer> romanDictionary = setUpRomanNumber();

    public int romanToInt(String s) {
        int romanNumber = 0;
        char[] cArr = s.toCharArray();

        for (int i = 0; i < cArr.length; i++) {
            if(i + 1 == cArr.length){ //if last index
                romanNumber += romanDictionary.get(cArr[i]);
                continue;
            }

            Integer currentNumber = romanDictionary.get(cArr[i]);
            Integer nextNumber = romanDictionary.get(cArr[i + 1]);

            if(currentNumber < nextNumber){
                romanNumber = romanNumber + (nextNumber - currentNumber);
                i++;
                continue;
            }

            romanNumber += romanDictionary.get(cArr[i]);
        }

        return romanNumber;
    }

    private static Map<Character, Integer> setUpRomanNumber(){
        Map<Character, Integer> romanDictionary = new HashMap<>();

        romanDictionary.put('I', 1);
        romanDictionary.put('V', 5);
        romanDictionary.put('X', 10);
        romanDictionary.put('L', 50);
        romanDictionary.put('C', 100);
        romanDictionary.put('D', 500);
        romanDictionary.put('M', 1000);

        return romanDictionary;
    }
}