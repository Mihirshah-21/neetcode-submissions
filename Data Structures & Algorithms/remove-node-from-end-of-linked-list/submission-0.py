# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        past = head
        N = 0
        while(curr):
            curr = curr.next
            N +=1
        new = N-n
        if new == 0:
            return head.next
        curr = head
        while (new !=0 and curr):
            past = curr
            curr = curr.next
            new -=1
        past.next = curr.next
        return head
    



        