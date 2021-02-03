# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or n==m:
            return head
        prev,nxt=None,head
        while m>1:
            prev=nxt
            nxt=nxt.next
            m-=1
            n-=1
        p,q,r=None,nxt,nxt.next
        while n>1:
            q.next=p
            p,q=q,r
            r=r.next
            n-=1
        q.next=p
        nxt.next=r
        if prev:
            prev.next=q
            return head
        return q