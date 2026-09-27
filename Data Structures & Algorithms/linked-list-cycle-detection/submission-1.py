# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        
        while head is not None:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False






















        
        # visited = set()
        # current = head

        # while current is not None:
        #     if current in visited:
        #         return True
        #     visited.add(current)
        #     current = current.next
        # return False
