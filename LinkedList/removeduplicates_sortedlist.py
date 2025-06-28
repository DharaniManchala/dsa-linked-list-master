class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def remove_duplicates(self):
        if not self.head:
            return 
        current=self.head
        while current and current.next:
            if current.data==current.next.data:
                current.next=current.next.next
            else:
                current=current.next
        
    def printList(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
l1 = LinkedList()
l1.head = Node(10)
second = Node(10)
third = Node(20)
fourth = Node(20)
fifth = Node(30)
l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
l1.printList()
l1.remove_duplicates()
l1.printList()
# time complexity-O(n)
# space complexity-O(1)
