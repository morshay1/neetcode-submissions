# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output_list = ListNode(0, None)
        head = output_list

        num_l1 = 0
        counter = 1
        while l1 is not None:
            num_l1 += counter * l1.val
            counter *= 10 
            l1 = l1.next

        num_l2 = 0
        counter = 1
        while l2 is not None:
            num_l2 += counter * l2.val
            counter *= 10 
            l2 = l2.next

        sum_num = num_l1 + num_l2

        if sum_num == 0:
            return head
            
        while sum_num > 0:
            output_list.next = ListNode(sum_num % 10, None)
            output_list = output_list.next
            sum_num = sum_num // 10

        return head.next
        
