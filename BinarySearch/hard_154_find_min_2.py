"""154. Find Minimum in Rotated Sorted Array II
Hard

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
"""

from typing import List

# 52ms, 80%, 15MB, 15%
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lt = 0
        rt = len(nums) - 1
        min_val = float("inf")
        while lt <= rt:
            min_val = min(min_val, nums[lt], nums[rt])
            lt += 1
            rt -= 1
        return min_val