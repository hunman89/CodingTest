class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0
        for n in nums:
            prev1 , prev2 = max(prev2 + n, prev1), prev1
        return prev1