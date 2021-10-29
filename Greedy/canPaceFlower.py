"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

"""
from typing import List

# RunTime: 156ms faster than 95.61%, Memory: 14.5MB, less than 62.06%
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count_flower = 0
        flowerbed_length = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, flowerbed_length+1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count_flower += 1
            
            if count_flower >= n:
                return True
        
        return False