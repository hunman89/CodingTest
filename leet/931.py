class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1,n):
            for j in range(n):
                if j - 1 >= 0:
                    left = matrix[i][j] + matrix[i-1][j-1]
                else:
                    left = float("inf")
                
                middle = matrix[i][j] + matrix[i-1][j]
                
                if j + 1 < n:
                    right = matrix[i][j] + matrix[i-1][j+1]
                else:
                    right = float("inf")
                matrix[i][j] = min(left, middle, right)
        return min(matrix[-1])