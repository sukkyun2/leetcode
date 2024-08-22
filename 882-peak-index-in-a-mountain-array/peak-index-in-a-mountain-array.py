class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_value, idx = float('-inf'), None
        for i, n in enumerate(arr):
            if n > max_value:
                max_value = n
                idx = i

        return idx