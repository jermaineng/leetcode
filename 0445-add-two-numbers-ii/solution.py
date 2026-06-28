# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = []
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        st2 = []
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        total = carry = 0
        dummy = None
        while st1 or st2 or carry:
            total = carry
            total += st1.pop() if len(st1) > 0 else 0
            total += st2.pop() if len(st2) > 0 else 0

            carry = total // 10
            total = total % 10
            
            new = ListNode(total)
            new.next = dummy
            dummy = new

        return dummy
            



