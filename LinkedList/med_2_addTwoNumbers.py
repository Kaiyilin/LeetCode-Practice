# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
""" 2 add to 
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional

# 68 ms, 78.12%; 14.4MB, 46%
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        ans = curr
        res = 0
        while l1 or l2:
            #print(curr)
            curr.next = ListNode()
            curr = curr.next
            l1_val, l2_val = 0, 0
            if l1:
                l1_val = l1.val
                l1 = l1.next      
            if l2:
                l2_val = l2.val
                l2 = l2.next
                
            val = (l1_val + l2_val + res) % 10
            res = (l1_val + l2_val + res) // 10 
            curr.val = val  
            
        if res:
            curr.next = ListNode(res)
        return ans.next