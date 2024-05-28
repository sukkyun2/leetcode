class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, history = 0, set()
        for i in range(len(nums)):
            if nums[i] not in history:
                history.add(nums[i])
                nums[curr] = nums[i]
                curr += 1

        return len(history)
        