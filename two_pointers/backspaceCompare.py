"""Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 
"""

# RunTime: 20ms, 99.36% 
# Memory: 14.1MB, 79.81%
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []

        def pop_stack(stack):
            if stack:
                stack.pop()
            else:
                pass

        for ele in s:
            if ele == "#":
                pop_stack(stack_s)
            else:
                stack_s.append(ele)
        
        for ele in t:
            if ele == "#":
                pop_stack(stack_t)
            else:
                stack_t.append(ele)
        return stack_s == stack_t
