"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

"""
# Thoughts
# create a alphabet count table
# if the alphabet count are match, then True else false

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransome_note_table = Counter(ransomNote)
        magazine_table = Counter(magazine)

        for key in ransome_note_table:
            if key not in magazine_table or magazine_table[key] < ransome_note_table[key]:
                return False
        
        return True