class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for i in range(len(text1))]
        def LCS(text1, text2, index_text1, index_text2):
            if index_text1 == len(text1) or index_text2 == len(text2):
                return 0
            if (dp[index_text1][index_text2] > 0):
                return dp[index_text1][index_text2]

            if (text1[index_text1] == text2[index_text2]):
                dp[index_text1][index_text2] = 1 + LCS(text1, text2, index_text1+1, index_text2+1)
                return dp[index_text1][index_text2]
            else:
                dp[index_text1][index_text2] = max(LCS(text1, text2, index_text1+1, index_text2), LCS(text1, text2, index_text1, index_text2 + 1))
                return dp[index_text1][index_text2]
        return LCS(text1, text2, 0, 0)
