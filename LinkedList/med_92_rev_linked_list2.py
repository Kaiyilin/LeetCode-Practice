"""92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""
from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 28 ms, 89%  14.4 MB, 71%
class Solution:
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        start_idx = left -1
        end_idx = right - 1
        
        while start_idx < end_idx:
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
            start_idx += 1
            end_idx -= 1
        
        dummy = ListNode()
        ans = dummy
        
        queue = deque(arr)
        
        while queue:
            val = queue.popleft()
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        return ans.next

