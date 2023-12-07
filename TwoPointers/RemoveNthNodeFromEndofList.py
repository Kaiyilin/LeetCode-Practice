"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""

# Using 2 pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialise 2 pointers
        fast = head
        slow = head
        # Set fast pointer to kth position
        # than the slow pointer 
        for i in range(n):
            fast = fast.next
        
        # While the fast pointer is finished
        # The slow pointer will locate ate the position
        # where you'd like to remove
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # fail to handle Example 2 and Example 3
        # I must ignored some condition
        slow.next = slow.next.next

        return head