"""Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""
from typing import List

# Pass the example cases, fail on tests
# RunTime error, sorted took lots of time
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_width = len(p)
        str_len = len(s)
        sorted_p = sorted(p)
        locations = []
        i = 0
        
        if str_len < window_width:
            return []
        
        while (i + window_width) <= str_len:
            if sorted(s[i:(i + window_width)]) == sorted_p:
                locations.append(i)
                i += 1
            else: 
                i += 1
        return locations

# Using hash map, check the freq first 
# Run Time Error
# the problem happened in the while loop, any possible solution 
# to maintain the window size and adjust the freq table simutaneously ?
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_width = len(p)
        str_len = len(s)
        freq_p = {}
        locations = []
        i = 0
        for char in p:
            freq_p[char] = freq_p.get(char, 0) + 1 # dictionary.get(keyname, value) value is optional if certain key not exist, assign that value

        if str_len < window_width:
            return []

        freq_s = {}
        while (i + window_width) <= str_len:
            sub_seq = s[i:(i + window_width)]
            for char in sub_seq:
                freq_s[char] = freq_s.get(char, 0) + 1
            
            if sorted(freq_s.items()) == sorted(freq_p.items()):
                locations.append(i)
                #print(locations, i)
                i += 1 
            else:
                i += 1
                
        return locations

# Example Case
s = "cbaebabacd"
p = "abc"

sol = Solution2()
print(sol.findAnagrams(s, p))

# Test Case 
s = "ababababab"
p = "aab"

sol = Solution2()
print(sol.findAnagrams(s, p))