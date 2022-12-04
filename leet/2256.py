class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sums = list(accumulate(nums))
        answer = [inf, inf]
        for i in range(n := len(nums)):
            left_avg = sums[i] // (i+1)
            right_avg = (sums[-1] - sums[i]) // (n-i-1) if (n-i-1) != 0 else 0
            ab = abs(left_avg - right_avg)
            answer = min(answer, [ab,i])
        return(answer[1])
        
        # sum_all, left_sum = sum(nums), 0
        # answer = [inf, inf]
        # for i in range(n := (len(nums))):
        #     left_sum += nums[i]
        #     right_sum = sum_all - left_sum
        #     left_avg = left_sum // (i+1)
        #     right_avg = right_sum // (n-i-1) if (n-i-1) != 0 else 0
        #     ab = abs(left_avg - right_avg)
        #     answer = min(answer, [ab,i])
        # return(answer[1])
