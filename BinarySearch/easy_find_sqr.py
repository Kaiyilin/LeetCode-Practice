class Solution:
    def mySqrt(self, x: int) -> int:
        # Newto's method
        e = x 
        while (e * e) > x:
            e = (e + x/e) // 2

        return int(e)

sol = Solution()
sol.mySqrt(2147395600)
sol.mySqrt(5)