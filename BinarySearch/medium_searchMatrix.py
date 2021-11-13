from typing import List

"""Write an efficient algorithm that searches for a value in an m x n matrix. 

This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
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
        return False 



sol = Solution()
# Test case:
## true
matrix = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]
target = -5
print(sol.searchMatrix(matrix=matrix, target=target))

## false
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(sol.searchMatrix(matrix=matrix, target=target))

## true
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix=matrix, target=target))