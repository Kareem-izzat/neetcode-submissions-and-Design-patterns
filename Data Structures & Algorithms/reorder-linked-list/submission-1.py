class Solution:
    def reorderList(self, l1: Optional[ListNode]) -> None:
        slow = l1
        fast = l1.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        rev = self.reverseList(l2)

        l1p = l1
        while rev:
            tmp = l1p.next
            nxt = rev
            rev = rev.next
            l1p.next = nxt
            l1p.next.next = tmp
            l1p = tmp

    def reverseList(self, head):
        if head is None:
            return None

        p1 = head
        p2 = head.next
        p1.next = None

        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp

        return p1