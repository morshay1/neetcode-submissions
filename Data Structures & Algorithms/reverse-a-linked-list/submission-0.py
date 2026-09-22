# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        elif head.next.next is None:
            butt = head.next
            butt.next = head
            head.next = None
            return butt
        else:
            prev = head
            curr = head.next
            ahead = head.next.next
            prev.next = None
            while ahead is not None:
                curr.next = prev
                prev = curr
                curr = ahead
                ahead = ahead.next
            curr.next = prev
            return curr

