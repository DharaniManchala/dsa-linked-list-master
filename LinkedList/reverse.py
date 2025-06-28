class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverse(self):
        prev=None
        current=self.head
        while current:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        self.head=prev
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
l1 = LinkedList()
l1.head = Node(10)
second = Node(20)
third = Node(30)
l1.head.next = second
second.next = third
l1.printList()  # Output: 10 -> 20 -> 30 -> None
l1.reverse()
l1.printList()  # Output: 30 -> 20 -> 10 -> None
# time complexity of reverse is O(n) where n is the number of nodes in the linked list
# space complexity is O(1) as we are using constant space for the prev, current, and nextnode pointers
# Note: The reverse function modifies the linked list in place, reversing the order of nodes.
