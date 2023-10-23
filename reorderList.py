# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodeArr = []
        it = head
        while it:
            nodeArr.append(it)
            it = it.next
        l, r = 0, len(nodeArr)-1
        while l < r:
            nodeArr[r].next = nodeArr[l].next
            nodeArr[l].next = nodeArr[r]
            l += 1
            r -= 1
        nodeArr[l].next = None
