"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
# 32ms, 75%
# 14.2 MB, 80% 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        if not root:
            return res
        # The very first element of the queue
        # is the right most node in our tree 
        queue.append(root)

        while queue:
            size = len(queue)
            res.append(queue[0].val)

            for _ in range(size):
                current = queue.popleft()
                # right first
                if current.right:
                    queue.append(current.right)
                
                # if right side is empty and lt side exist
                # then you can see the val in left side
                if current.left:
                    queue.append(current.left)
        return res
        