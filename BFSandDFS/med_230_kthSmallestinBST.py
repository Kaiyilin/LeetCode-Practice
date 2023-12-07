"""230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 52 ms, 65%, 18.1MB, 61%
class Solution:
    def post_traversal(self, node, rec):
        if node:
            self.post_traversal(node.left, rec)
            rec.append(node.val)
            self.post_traversal(node.right, rec)
            
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rec = []
        self.post_traversal(root, rec)
        #print(rec)
        return rec[k-1]