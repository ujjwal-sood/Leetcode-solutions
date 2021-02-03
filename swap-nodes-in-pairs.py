# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        f,s=head,head.next
        tail=self.swapPairs(head.next.next)
        f.next=tail
        s.next=f
        return s