class Solution:
    def minMaxGame(self, nums: List[int]) -> int: 
        while len(nums) != 1:
            print(nums)
            new_nums = []
            for i in range(0, len(nums), 2):
                func = max if i // 2 % 2 else min   
                new_nums.append(func(nums[i],nums[i+1]))
            nums = new_nums
        
        return nums[0]
        