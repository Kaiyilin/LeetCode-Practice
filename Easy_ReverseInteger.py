"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0 
        elif x > 0:
            str_x = str(x)
            reveser_x = int(str_x[::-1])
        else:
            x = (-1) * x 
            str_x = str(x)
            reveser_x = (-1)* (int(str_x[::-1]))
        
        if not -(2**31) < reveser_x < 2**31:
            return 0
        else:
            return reveser_x

    # Logs         
    # Runtime: 32 ms, faster than 71.53% of Python3 online submissions for Reverse Integer.
    # Memory Usage: 14.3 MB, less than 13.43% of Python3 online submissions for Reverse Integer.

    # Try different approach  
    def reverse2(self, x: int) -> int:
        if x == 0:
            return 0 
        elif x > 0:
            str_x = str(x)
            reveser_x = int(str_x[::-1])
        else:
            x = (-1) * x 
            str_x = str(x)
            reveser_x = (-1)* (int(str_x[::-1]))
        
        if not -(2**31) < reveser_x < 2**31:
            return 0
        else:
            return reveser_x
        