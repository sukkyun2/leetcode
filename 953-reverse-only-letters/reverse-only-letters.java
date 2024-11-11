class Solution {
    public String reverseOnlyLetters(String s) {
        char[] arr = s.toCharArray();
        int front = 0, rear = arr.length-1;
        
        while(front<=rear){
            if(!Character.isLetter(arr[front])){
                front++;
                continue;
            } else if(!Character.isLetter(arr[rear])){
                rear--;
                continue;
            }

            //swap
            char tmp = arr[front];
            arr[front] = arr[rear];
            arr[rear] = tmp;
            
            front++;
            rear--;
        }

        return String.valueOf(arr);       
    }
}