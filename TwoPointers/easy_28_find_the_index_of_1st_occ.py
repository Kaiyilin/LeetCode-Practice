"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

def strStr(haystack: str, needle: str) -> int:
    
    if not needle:
        return -1
    
    len_haystack = len(haystack)
    len_needle = len(needle)

    if len_haystack < len_needle:
        return -1

    for idx in range(len_haystack - len_needle + 1):
        if haystack[idx:idx + len_needle] == needle:
            return idx

    return -1 # needle not found

haystack = "sadbutsad"
needle = "sad"

# should be 0 
print(strStr(haystack, needle))

# should be -1 
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))

# should be 4 but return -1
haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle))

haystack = "a"
needle = "a"
print(strStr(haystack, needle))

haystack = "a"
needle = "ad"
print(strStr(haystack, needle))