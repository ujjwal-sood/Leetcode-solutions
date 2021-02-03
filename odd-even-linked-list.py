# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ev = ListNode(-1)
        odd = ListNode(-1)
        
        tmpev = ev
        tmpodd = odd
        
        tmp = head
        ctr = 0
        while tmp:
            if ctr & 1:
                tmpodd.next = tmp
                tmpodd = tmpodd.next
            else:
                tmpev.next = tmp
                tmpev = tmpev.next
            tmp = tmp.next
            ctr += 1
        
        tmpev.next = odd.next
        tmpodd.next = None
        return ev.next