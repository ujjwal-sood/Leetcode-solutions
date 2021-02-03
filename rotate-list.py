# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        c=0
        temp=head
        while temp:
            temp=temp.next
            c+=1
        if k%c==0:
            return head
        k=k%c
        temp,nxt=head,head
        while k:
            nxt=nxt.next
            k-=1
        while nxt.next:
            temp=temp.next
            nxt=nxt.next
        nxt.next=head
        head=temp.next
        temp.next=None
        return head