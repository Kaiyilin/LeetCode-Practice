"""109. Convert Sorted List to Binary Search Tree
Medium

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 

Example 1:

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [0]
Output: [0]

Example 4:

Input: head = [1,3]
Output: [3,1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# wrong answer, it will generate unbalanced tree
class Solution:    
    def insert_helper(self, start: TreeNode, val):
        """Recursively insert the values
        """
        if start.val < val:
            if start.right:
                self.insert_helper(start.right, val)
            else:
                start.right = TreeNode(val)
        elif start.val == val:
            pass
        
        else:
            if start.left:
                self.insert_helper(start.left, val)
            else:
                start.left = TreeNode(val)
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        
        # convert linked list to array
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        # set the middle on as the root
        root = TreeNode(arr[len(arr) // 2])
        print(root)
        
        # create a binary search tree
        while arr:
            val = arr.pop()
            self.insert_helper(root, val)
        
        return root

# 124ms, 90%; 20.4MB, 37%
class Solution:    
    def BSTconstructor(self, arr):
        """Recursively constructed the BST
        """
        if not arr:
            return None
        mid = len(arr) // 2
        val = arr[mid]
        
        tree = TreeNode(val)
        tree.left = self.BSTconstructor(arr[:mid])
        tree.right = self.BSTconstructor(arr[mid+1:])

        return tree
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        
        # convert linked list to array
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        # construct balance BST
        root = self.BSTconstructor(arr=arr)
        
        return root