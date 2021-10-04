"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order. 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

# Solution1
# run time 288 ms memory 16 MB
def sortedSquares(nums: List[int]) -> List[int]:
    # all i need to care about in this problem
    # is whether the square of neg values are greater 
    # than the sqr of positive values
    
    # Set up 2 pointers
    # right is the index of first non-neg value 
    # left is the index of the last neg value
    right = 0
    while right<len(nums) and nums[right]<0:
        right += 1
    left = right-1
    ans = []
    while left >= 0 and right < len(nums):
        if nums[left]**2 > nums[right]**2:
            # when right is smaller, 
            # append it and move the right pointer
            ans.append(nums[right]**2)
            right += 1
        else:
            ans.append(nums[left]**2)
            left -= 1
    while left >=0:
        ans.append(nums[left]**2)
        left -= 1
    while right < len(nums):
        ans.append(nums[right]**2)
        right += 1
    return ans

# Solution2 with numpy
# run time 491 ms memory 32.7 MB
def sortedSquares(nums: List[int]) -> List[int]:
    import numpy as np 
    ans = np.multiply(nums, nums)
    sort_ans = sorted(ans)
    return sort_ans