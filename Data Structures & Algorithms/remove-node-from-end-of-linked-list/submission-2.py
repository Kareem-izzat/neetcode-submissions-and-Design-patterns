# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None or head.next == None:
            return None
        

        size = 0
        s = head

        while s:
            size += 1
            s = s.next

        before = size - n

        # remove head
        if before == 0:
            return head.next

        count = 1
        p = head

        while count < before:
            p = p.next
            count += 1

        p.next = p.next.next

        return head

                