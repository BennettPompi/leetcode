class cacheNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = None
    
    def printCache(self):
        ptr = self.head
        print("CACHE(",self.cap,"):")
        if not ptr:
            print("[]")
        else:
            while ptr:
                print("Key: ", ptr.key, "Val: ", ptr.val)
                ptr = ptr.next

    def get(self, key: int) -> int:
        self.printCache()
        if not self.head:
            return
        targetPtr = None
        foundThisLoop = False
        if self.head.key == key:
            targetPtr = self.head
            if self.head.next:
                self.head = self.head.next
        fast = self.head.next
        slow = self.head
        while fast:
            if fast.key == key:
                targetPtr = fast
                foundThisLoop = True
                if fast.next:
                    slow.next = fast.next
            fast = fast.next
            if not foundThisLoop:
                slow = slow.next
            else:
                foundThisLoop = False
        if targetPtr:
            targetPtr.next = None
            slow.next = targetPtr
            return targetPtr.val
        else: return -1


    def put(self, key: int, value: int) -> None:
        self.printCache()
        newNode = cacheNode(key, value)
        ptr = self.head
        while ptr and ptr.next:
            ptr = ptr.next
        if ptr:
            ptr.next = newNode
        else:
            self.head = newNode
        if self.size == self.cap:
            self.head = self.head.next
        else:
            self.size += 1
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)