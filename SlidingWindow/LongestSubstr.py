"""Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""



# Run Time: 80 ms (50%), Memory: 14.4 MB (50%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mystr = s
        max_sublength = 0
        i = 0
        j = 1
        if len(mystr) < 2:
            return len(mystr)
        while j < len(mystr):
            if mystr[j] not in mystr[i:j] and mystr[j]:
                j+= 1
                max_sublength = max(max_sublength, len(mystr[i:j]))
            else:
                i += 1
        
        return max_sublength


# Test Case

a = Solution()

assert a.lengthOfLongestSubstring("abcabcbb") == 3
assert a.lengthOfLongestSubstring("bbbbb") == 1
assert a.lengthOfLongestSubstring("pwwkew") == 3
assert a.lengthOfLongestSubstring("") == 0
assert a.lengthOfLongestSubstring(" ") == 1
assert a.lengthOfLongestSubstring("     ") == 1