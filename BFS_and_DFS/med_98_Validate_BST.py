"""918 Validate BST

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

# wrong answer
class Solution:
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                if node.left.val < node.val:
                    queue.append(node.left)
                else:
                    return False
            
            if node.right:
                if node.right.val > node.val:
                    queue.append(node.right)
                else:
                    return False
        return True