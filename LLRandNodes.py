"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #create dict where key is original id and value is copyNode
        if not head:
            return None
        ogToCopy = {}
        curr = head
        while curr:
            newNode = Node(curr.val)
            ogToCopy[id(curr)] = newNode
            curr = curr.next
        curr = head
        headCopy = ogToCopy[id(head)]
        while curr:
            if curr.next:
                ogToCopy[id(curr)].next = ogToCopy[id(curr.next)]
            if curr.random:
                ogToCopy[id(curr)].random = ogToCopy[id(curr.random)]
            curr = curr.next
        return headCopy