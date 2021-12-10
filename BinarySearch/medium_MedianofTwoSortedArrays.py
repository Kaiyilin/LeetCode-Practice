"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
"""
from typing import List
from collections import Counter
# memory limit exceed
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # create a sorted, since
        merge = []
        while nums1 or nums2:
            #print(f"nums1: {nums1}")
            #print(f"nums2: {nums2}")
            #print(f"merge: {merge}")
            if not nums1 and nums2:
                while nums2:
                    ans = nums2.pop
                    merge.append(ans)
                    
            if nums1 and not nums2:
                while nums1:
                    ans = nums1.pop()
                    merge.append(ans)
                
            else:
                
                if nums1[-1] > nums2[-1]:
                    merge.append(nums1[-1])
                    nums1.pop()
                    
                else:
                    merge.append(nums2[-1])
                    nums2.pop()
        #print(merge)
        
        length = len(merge)
        if length % 2 == 0:
            return (merge[length // 2] + merge[length // 2 + 1]) / 2
        else:
            return merge[length // 2]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        merge = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1
        while i < m:
            merge.append(nums1[i])
            i += 1
        
        while j < n:
            merge.append(nums2[j])
            j += 1
            
        if (m+n) % 2 == 0:
            return (merge[(m+n) // 2] + merge[(m+n) // 2 - 1]) / 2
        else:
            return merge[(m+n) // 2]