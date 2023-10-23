class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1.val <= list2.val:
            head1 = list1
            head2 = list2
        else:
            head1 = list2
            head2 = list1
        next1 = head1.next
        next2 = head2.next
        while head1 and head2:
            print(head1.val, head2.val)
            if head2.val > next1.val:
                head1 = next1
                next1 = head1.next
                continue
            else:
                head1.next = head2
                head1 = head2
                head2 = next2
                if head2:
                    next2 = head2.next
                if head1:
                    head1.next = next1
        return head1