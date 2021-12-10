"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""
from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # find the nearby 4 directions with same vale "recursively"
        ROW_N = len(image)
        COLUMN_N = len(image[0])
        queue = deque()
        queue.append([sr, sc])
        impacted = []
        while queue:
            row, col = queue.popleft()
            if 0 <= row < ROW_N and 0 <= col < COLUMN_N:
                if image[row-1][col] == image[row][col]:
                    queue.append([row-1, col])
                    impacted.append([row-1, col])

                if image[row+1][col] == image[row][col]:
                    queue.append([row+1, col])
                    impacted.append([row+1, col])

                if image[row][col-1] == image[row][col]:
                    queue.append([row, col-1])
                    impacted.append([row, col-1])
                
                if image[row][col+1] == image[row][col]:
                    queue.append([row, col+1])
                    impacted.append([row, col+1])
            else:
                pass
        
        for ele in impacted:
            x, y = ele
            image[x][y] == newColor

#Output: [[2,2,2],[2,2,2]]
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0 
newColor = 2

sol = Solution()
sol.floodFill(image=image, sr=sr, sc=sc, newColor=newColor) 