# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        curr1, curr2 = l1, l2
        currSum = ListNode()
        headSum = currSum
        while curr1 or curr2:
            sum = 0
            if curr1:
                sum += curr1.val
            if curr2:
                sum += curr2.val
            if carry:
                sum += 1
                carry = False
            if sum >= 10:
                carry = True
                sum -= 10
            currSum.val = sum
            if (curr1 and curr1.next) or (curr2 and curr2.next):
                currSum.next = ListNode()
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            if currSum.next:
                currSum = currSum.next
        if carry:
            currSum.next = ListNode(1)
        return headSum
