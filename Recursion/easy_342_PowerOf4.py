
# 32ms 67%, 14.1MB, 90%
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n < 1:
            return False
        
        elif n == 1:
            return True
        
        else:
            return self.isPowerOfFour(n/4)

#math.log(16)
sol = Solution()
ans = sol.isPowerOfFour(16)
print(ans)