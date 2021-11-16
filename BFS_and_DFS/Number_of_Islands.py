"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        n_row = len(grid) 
        n_col = len(grid[0])
        
        def dfs(x, y):
            if x >= n_row or x < 0 or y < 0 or y >= n_col or grid[x][y] != "1" :
                return 
            grid[x][y] = "X"
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    n_islands += 1
        
        return n_islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

sol = Solution()
print(sol.numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(sol.numIslands(grid))