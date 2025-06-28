class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def middle_element(self):
        slow=self.head
        fast=self.head
        if fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data if slow else None
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
middle_value = l1.middle_element()
print(f"The middle element is: {middle_value}")  # Output: The middle element is: 20
# time complexity of middle_element is O(n) where n is the number of nodes in the linked list
# space complexity is O(1) as we are using constant space for the slow and fast