"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0

        length_w1 = len(word1)
        length_w2 = len(word2)
        output = ""
        counter = 0
        while p1 < length_w1 and p2 < length_w2:
            if counter % 2 == 0:
                output += word1[p1]
                p1 += 1
            else:
                output += word2[p1]
                p2 += 1

        while p1 < length_w1:
            output += word1[p1]
            p1 += 1
            
        while p2 < length_w2:
            output += word2[p1]
            p2 += 1
        return output

# passed
# 37 ms Beats 69.54% of users with Python3
# looks redundant can you simplify the code?