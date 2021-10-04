# 2 pointers opposite direction

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
        