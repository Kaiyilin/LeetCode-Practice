"""103. Binary Tree Zigzag Level Order Traversal
Medium

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import (
    Optional,
    List)
from collections import deque

# 28ms, 91.47% 14.3MB 98.16%
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []
        switch = True
        
        while queue:
            buffer = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                buffer.append(node.val)
            
            if switch:
                res.append(buffer)
                switch = False
            else:
                res.append(buffer[::-1])
                switch = True
        
        return res