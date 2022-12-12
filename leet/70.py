class Solution:
    def climbStairs(self, n: int) -> int:
        step_before = step_after = 1
        for i in range(n-1):
            step_after, step_before = step_after + step_before, step_after
        return step_after