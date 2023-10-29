public class MinStack {
    private Integer pointer;
    private List<Integer> minNumbers;
    private List<Integer> numbers;

    public MinStack() {
        numbers = new ArrayList<>();
        minNumbers = new ArrayList<>();
    }

    public void push(int val) {
        if(numbers.isEmpty()){
            minNumbers.add(val);
        } else {
            if(minNumbers.get(minNumbers.size() -1) >= val){
                minNumbers.add(val);
            }
        }

        numbers.add(val);
    }

    public void pop() {
        Integer val = numbers.get(numbers.size() - 1);

        if(val == getMin()){
            minNumbers.remove(minNumbers.size() -1);
        }

        numbers.remove(numbers.size() -1);
    }

    public int top() {
        return numbers.get(numbers.size() -1);
    }

    public int getMin() {
        return minNumbers.get(minNumbers.size() - 1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */