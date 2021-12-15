"""A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28

Example 4:

Input: m = 3, n = 3
Output: 6
"""

# Time limit exceed
class Solution:
    
    def helper(self, m: int, n: int, memo={}):
        
        key = (m, n)
        key2 = (n, m)
        
        if key not in memo and key2 in memo:
            memo[key] = memo[key2]

        if key in memo:
            return memo[key]

        if m == 0 or n == 0:
            return 0

        if m ==1 and n == 1:
            return 1
        
        return self.helper(m-1, n) + self.helper(m, n-1)
        
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.helper(m, n)

# 36ms, 26%; 14.4MB, 39%
class Solution:
    
    def helper(self, m: int, n: int, memo={}):
        
        key = (m, n)
        key2 = (n, m)
        
        if key not in memo and key2 in memo:
            memo[key] = memo[key2]

        if key in memo:
            return memo[key]

        if m == 0 or n == 0:
            return 0

        if m ==1 and n == 1:
            return 1
        
        memo[key] = self.helper(m-1, n) + self.helper(m, n-1)
        return memo[key]
        
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.helper(m, n)
         


sol = Solution()
print(sol.uniquePaths(23, 12))
