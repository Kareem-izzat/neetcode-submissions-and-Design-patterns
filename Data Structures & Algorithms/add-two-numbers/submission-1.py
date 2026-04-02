# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def size(list):
            size=0
            while list != None:
                size+=1
                list = list.next
            return size
        def appendLast(list,val):
            newNode = ListNode(val)
            p=list
            while p.next!= None:
                p = p.next
            p.next = newNode

        size1=size(l1)
        size2=size(l2)
        if size1<size2:
            l1,l2 = l2,l1
        carry=0
        p=l1
        while l2!=None:
            if l2.val + l1.val + carry <10:
                l1.val=l2.val+l1.val + carry
                l1=l1.next
                l2=l2.next
                carry=0
            else:
                l1.val=(l2.val+l1.val + carry) %10
                carry=1
                l1 = l1.next
                l2 = l2.next
        while carry ==1:
            if l1:
                if l1.val + carry <10:
                    l1.val=l1.val + carry
                    l1=l1.next
                    carry=0
                else:
                    l1.val=0
                    l1=l1.next
            else:
                appendLast(p,1)
                carry=0
        return p

        