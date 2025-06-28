class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def detect_and_remove_loop(self):
        if not self.head or not self.head.next:
            return False
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print("loop detected")
                prev=None
                slow=self.head
                while slow!=fast:
                    prev=fast
                    slow=slow.next
                    fast=fast.next
                prev.next=None
                return True
        print("no loop detected")
        return False
    def printList(self):
        current=self.head
        visited=set()
        while current:
            if id(current)in visited:
                print("loop detected")
                return
            visited.add(id(current))
            print(current.data, end="->")
            current=current.next
        print("None")
l1=LinkedList()
l1.head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
fifth=Node(50)
l1.head.next=second
second.next=third
third.next=fourth
fourth.next=fifth
# Creating a loop for testing
fifth.next=second  # Loop back to second node
l1.printList()
if l1.detect_and_remove_loop():
    print("Loop removed.")
else:
    print("No loop to remove.")
l1.printList()
# time complexity-O(n)
# space complexity-O(1)