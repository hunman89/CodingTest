from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        if not word:
            return True
        if len(word) > m * n:
            return False
        
        counter = Counter(word)
        for line in board:
            for char in line:
                if char in counter:
                    counter[char] -= 1
        for value in counter.values():
            if value > 0:
                return False
        
        def dfs(row, col, word):
            if not word:
                return True
            if 0 <= row < m and 0 <= col < n and board[row][col] == word[0]:
                board[row][col] = '#'
                for dr, dc in [(row, col+1), (row+1, col), (row, col-1), (row-1,col)]:
                    if dfs(dr, dc, word[1:]):
                        return True
                board[row][col] = word[0]
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r,c,word):
                    return True
        return False