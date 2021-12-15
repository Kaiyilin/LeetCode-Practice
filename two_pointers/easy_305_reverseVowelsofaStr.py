"""345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

"""

# Same Logic with different data structure resulted in different time 

# using list to store vowels
# 76ms, 32%; 17MB 36%
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        
        # str can't be swap in python, turn it into list
        s = list(s)
        start_p = 0
        end_p = len(s) - 1
        
        while start_p < end_p:
            
            if s[start_p] in vowels and s[end_p] in vowels:
                s[start_p], s[end_p] = s[end_p], s[start_p]
                start_p += 1
                end_p -= 1
            
            elif s[start_p] in vowels and s[end_p] not in vowels:
                end_p -= 1
            
            elif s[start_p] not in vowels and s[end_p] in vowels:
                start_p += 1
            
            else:
                start_p += 1
                end_p -= 1
        # 4ms difference compared to
        # "".join(s) 
        ans = "".join(ele for ele in s)
        return ans
sol = Solution()
print(sol.reverseVowels(".,"))

# using set to store vowels
# 44ms, 95%, 15MB 48%
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AaEeIiOoUu")
        #print(vowels)
        # str can't be swap in python, turn it into list
        s = list(s)
        start_p = 0
        end_p = len(s) - 1
        
        while start_p <= end_p:
            
            if s[start_p] in vowels and s[end_p] in vowels:
                s[start_p], s[end_p] = s[end_p], s[start_p]
                start_p += 1
                end_p -= 1
            
            elif s[start_p] in vowels and s[end_p] not in vowels:
                end_p -= 1
            
            elif s[start_p] not in vowels and s[end_p] in vowels:
                start_p += 1
            
            else:
                start_p += 1
                end_p -= 1
        
        ans = "".join(s)
        return ans