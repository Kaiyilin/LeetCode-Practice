# 2 pointers opposite direction
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. 
The 0 is only there to ensure the merge result can fit in nums1.
"""
# Approach 1
# But it used other memory in computer the space != O(1)
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_pointer = 0
    nums2_pointer = 0
    output = []
    while nums1_pointer < m and nums2_pointer < n:
        if nums1[nums1_pointer] < nums2[nums2_pointer]:
            output.append(nums1[nums1_pointer])
            nums1_pointer += 1
            print(f"{output},m: {m}, nums_1 pointer: {nums1_pointer}")
        else:
            output.append(nums2[nums2_pointer])
            nums2_pointer += 1
            print(f"{output},n: {n}, nums2_pointer: {nums2_pointer}")
    
    while nums1_pointer<m:
        output.append(nums1[nums1_pointer])
        nums1_pointer += 1
        
    while nums2_pointer<n:
        output.append(nums2[nums2_pointer])
        nums2_pointer += 1
    return output

# Cheated
# RunTime: 32 ms Memory: 14.1 MB
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_pointer = m
    nums2_pointer = 0
    output = []
    while nums2_pointer < n:
        nums1[nums1_pointer] = nums2[nums2_pointer]
        nums1_pointer += 1
        nums2_pointer += 1
    nums1.sort()


# 2 pointers
# RunTime: 32 ms Memory: 14.5 MB
def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Set pointers
    i = m - 1 # point to the m position of nums1
    j = n - 1 # point to the last position of nums2
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1