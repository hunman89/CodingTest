class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]

        # cache = [0, 1, 1]
        # for i in range(n // 3):
        #     a = cache[0] + cache[1] + cache[2]
        #     cache = [a, 2*a-cache[0], 3*a -cache[0] + cache[-1]]
        # return cache[n % 3]
        
        # cache = [0, 1, 1, 2]
        # while len(cache) <= n:
        #     cache.append(cache[-1] + cache[-2] + cache[-3])
        # return cache[n]