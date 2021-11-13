from typing import List

""" Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

# attempt 1, fail on ex3
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # ascending order 
        nums_len = len(nums)
        start = 0
        end = nums_len - 1 
        if nums_len == 0:
            return [-1, -1]
        elif nums_len == 1 and nums[0] == target:
            return [0, 0]
        
        while start < end:
            mid = (start + end) // 2 
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                if nums[mid-1] == target:
                    return [mid-1, mid]
                else:
                    return [mid, mid+1]
                
        return [-1, -1]

# Passed
class Solution_2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def srch_left(nums, target, left, right):
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid

            if nums[left] == target:
                return left
            
            if nums[right] == target:
                return right
            return -1
        
        def srch_right(nums, target, left, right):
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid

            if nums[right] == target:
                return right
            
            if nums[left] == target:
                return left
            return -1

        nums_len = len(nums)
        start = 0
        end = nums_len - 1 
        if nums_len == 0:
            return [-1, -1]
        result_lt = srch_left(nums=nums, target=target, left=start, right=end)

        if result_lt != -1:
            result_rt = srch_right(nums=nums, target=target, left=start, right=end)
        else:
            result_rt = -1
        
        return [result_lt, result_rt]

# ex1 expected [3, 4]
nums = [5,7,7,8,8,10]
target = 8

# ex2 expected [0, 0]
nums_2 = [1]
target_2 = 1

# ex3 expected [0, 1]
nums_3 = [2, 2]
target_3 = 2

solution = Solution()
print(solution.searchRange(nums=nums, target=target))
print(solution.searchRange(nums=nums_2, target=target_2))
print(solution.searchRange(nums=nums_3, target=target_3))

sol_2 = Solution_2()
print(sol_2.searchRange(nums=nums, target=target))
print(sol_2.searchRange(nums=nums_2, target=target_2))
print(sol_2.searchRange(nums=nums_3, target=target_3))
