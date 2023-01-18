class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        
        max_sum = nums[0]
        min_sum = 0
        res = nums[0]
        for i in range(1,len(nums)):
            max_sum = max(max_sum+nums[i], nums[i])
            min_sum = min(min_sum+nums[i], nums[i])
            res = max(res, max_sum, sum_nums - min_sum)
        return res