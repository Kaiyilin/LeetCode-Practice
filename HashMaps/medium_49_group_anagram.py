"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
    
"""

# approach: 
# sorted the individual string, and use it as the key
# each key correspond with a list 

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) < 2:
        return [strs]

    anagram_mapping = {}
    for word in strs:
        word_key = ''.join(sorted(word))
        if word_key not in anagram_mapping:
            anagram_mapping[word_key] = [word]
        else:
            anagram_mapping[word_key].append(word)
    
    output = []
    for key in anagram_mapping:
        output.append(anagram_mapping[key])
    return output


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))