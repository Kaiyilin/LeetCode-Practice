"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

# Two strings are isomorphic only if the mapping is 1-to-1 and bijective
# (meaning both s to t and t to s have 1-to-1 mappings).

def isIsomorphic(s: str, t: str) -> bool:
    mapping_table = {}

    for idx in range(len(s)):
        s_char, t_char = s[idx], t[idx]
        if s_char in mapping_table and mapping_table[s_char] != t_char:
            return False
        elif s_char not in mapping_table and t_char in mapping_table.values(): 
            # if t_char alreadt in mapping_table but not s_char, 
            # then it's not 1-to-1 mapping directly
            return False
        else:
            mapping_table[s_char] = t_char
    
    return True


# expected False
s = 'badc'
t = 'baba'

print(isIsomorphic(s, t))