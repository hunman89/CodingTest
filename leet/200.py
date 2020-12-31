from typing import List

grid = [
 ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


def numIslands(grid: List[List[str]]) -> int:  
  def dfs(i, j):
    if i < 0 or i >= len(grid) or j <0 or j >= len(grid[0]) or grid[i][j] != '1':
      return
    # 한번 방문한 점을 0으로 변경하여 방문 확인  
    grid[i][j] = 0
    
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
  
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '1':
        dfs(i,j)
        count += 1
  return count

print(numIslands(grid))
