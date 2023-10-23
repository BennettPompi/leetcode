class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Definition for singly-linked list.
        # class ListNode(object):
        #     def __init__(self, x):
        #         self.val = x
        #         self.next = None
       
       #using id to simulate pointer*
        """
        intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
        listA - The first linked list.
        listB - The second linked list.
        skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
        skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
        """
        listA, listB= headA, headB
        skipA,skipB, intersectVal= 0,0,0

        if (id(headA) == id(headB)):
            intersectVal = headA.val
            return intersectVal, listA, listB, skipA, skipB
        
        currentNode = headA
        nodesTraversed = {[]} #key: node ID, value: [node.val, aSkips]
        skipCount = 0
        while currentNode != None:
            nodesTraversed[id(currentNode)] = skipCount

        currentNode = headB
        skipCount = 0
        while (id(currentNode) not in  nodesTraversed) and (currentNode != None):
                currentNode = currentNode.next
                skipCount += 1
        if currentNode != None:
             intersectVal = currentNode.val
             skipA = nodesTraversed[id(currentNode)]
             skipB = skipCount         


        return intersectVal, listA, listB, skipA, skipB