class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
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
l1.insert_at_end(40)
l1.printList()  # Output: 10 -> 20 -> 30 ->40 -> None
# time complexity of insert_at_end is O(n) where n is the number of nodes in the linked list
# space complexity is O(1) as we are using constant space for the new_node pointer