from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        condition = len(nums) // 3
        counter = Counter(nums)

        return [k for k, v in counter.items() if v > condition]

        