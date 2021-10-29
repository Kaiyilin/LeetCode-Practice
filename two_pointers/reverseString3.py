"""
Given a string s, reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 
Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""


def reverseWords(s: str) -> str:
    i = 0
    j = 0
    buffer = []
    output = ""
    # check the space first
    while j < len(s):
        if s[j] == " ":
            if i == 0:
                buffer.append(s[j-1::-1])
                i = j
                j += 1 
            else:
                buffer.append(s[j-1: i: -1])
                i = j
                j += 1 
        elif j == len(s) -1:
            buffer.append(s[j: i: -1])
            i = j
            j += 1 
        else:
            j += 1
    print(j)
    print(buffer)
    for ele in buffer:
        output += ele + " "
    
    return output[:-1]

s = "Let's take LeetCode contest"

print(reverseWords(s))

#assert reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"

# Use pre-defined function
# RunTime:52 ms Memory: 15.2 MB
def reverseWords(self, s: str) -> str:
    buffer = s.split(" ")
    output = ""
    for ele in buffer:
        output += ele[::-1] + " "
    return output[:-1]