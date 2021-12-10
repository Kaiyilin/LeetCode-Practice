"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

a = [3, 1]

sol = Solution()
sol.search(a, 1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        s = 0
        t = len(nums) - 1 
        
        while s <= t:
            mid = (s + t) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[s] <= nums[mid]:
                if nums[s] <= target <= nums[mid]:
                    t = mid -1
                else:
                    s = mid + 1
            else:
                if nums[mid] <= target <= nums[t]:
                    s = mid + 1
                else:
                    t = mid - 1
        
        return -1

sol = Solution()
sol.search(a, 1)