import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = Arrays.stream(candies).max().orElse(0);

        return Arrays.stream(candies)
            .mapToObj(Integer::new)
            .map(candy->candy+extraCandies >= max)
            .collect(Collectors.toList());
    }
}