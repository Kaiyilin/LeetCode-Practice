from typing import List

"""240
Write an efficient algorithm that searches for a target value in an m x n integer matrix. 

The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #row_c = len(matrix)
        #col_c = len(matrix[0])
        if not matrix or not matrix[0]: 
            return False
        
        # O(row_c + log(col_c)), dominated by linear one
        for row in matrix:
            if row[0] == target or row[-1] == target:
                return True
            elif row[0] < target < row[-1]:
                return self.b_srch(row, target)
            else:
                pass
        return False
    
    def b_srch(self, array: List, target: int):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if target == array[mid]:
                return True
            
            elif target > array[mid]:
                left = mid + 1
            
            else:
                right = mid - 1
        pass 



sol = Solution()
# Test case:
## true
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(sol.searchMatrix(matrix=matrix, target=target))

## false
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(sol.searchMatrix(matrix=matrix, target=target))