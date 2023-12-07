"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""

from collections import deque
from typing import Optional

# Runtime 36ms, 93.07%, Memory 15.3MB, 96.03%
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = deque()
        if not root:
            return 0
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            depth += 1 
        
        return depth