class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] % 10

        new_nums = [nums[i] + nums[i + 1] for i in range(len(nums) - 1)]        
        return self.triangularSum(new_nums)
            
        