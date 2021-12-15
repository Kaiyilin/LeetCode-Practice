"""203 Remove the Linked List Element

Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# 64 ms	89%, 17.2 MB, 27%
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return None
        # create a dummy node in case the
        # head is target 
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = dummy.next
        ans = dummy

        # if you're not looping the whole list kepp going
        while curr:
            # if the curr.val == val
            # link the prev.next to curr.next
            # move the curr to next element 
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else: # move forward the prev and curr
                prev = prev.next
                curr = curr.next
        return ans.next