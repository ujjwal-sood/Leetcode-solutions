# Definition for singly-linked list.
"""class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
"""

class Solution:
    def fmid(self,head):
        first=head
        second=head.next.next
        while second and second.next:
            first=first.next
            second=second.next.next
        second=first.next
        first.next=None
        return second
    
    def reverse(self,head):
        if not head or not head.next:
            return head
        p,q,r=None,head,head.next
        while r:
            q.next=p
            p=q
            q=r
            r=r.next
        q.next=p
        return q
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        mid=self.fmid(head)
        t=self.reverse(mid)
        p,q,r=head,t,head.next
        while (q):
            p.next=q
            p=p.next
            q=r
            r=p.next
        return