"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# idea 1: using hash and count to see if the element are all valid
# idea 2: convert the string to unit-code then check the summation, got issue when s = 'ac', t = 'bb'
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    s_map = Counter(s)
    t_map = Counter(t)


    return s_map == t_map

# Output: true
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))


# Output: false
s = "rat"
t = "car"
print(isAnagram(s, t))