"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""
# Loop twice, to find out all the non zeros and append them
# and to find out all the zeros and append them

# RunTime: 280 ms, Memory: 15.7 MB
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # create the first pointer to look up the 
    # whole array
    length = len(nums)
    for i in range(length):
        if nums[i] != 0:
            nums.append(nums[i])
    
    for i in range(length):
        if nums[0] == 0:
            nums.append(nums[0])
            nums.pop(0)
        else:
            nums.pop(0)

# Second approach, two pointers
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 # slow
        j = 0 # fast
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1