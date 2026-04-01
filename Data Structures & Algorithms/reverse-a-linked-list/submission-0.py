# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        p1=head
        p2=head.next
        p1.next=None
        while p2!=None:
            temp = p2.next
            p2.next = p1
            p1=p2
            p2=temp
        start=p1
        return p1