class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def countnodes(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    def printList(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current=current.next
        print("None")
l1 = LinkedList()
l1.head = Node(10)
second = Node(20)
third = Node(30)
l1.head.next = second
second.next = third
l1.printList()  # Output: 10 -> 20 -> 30 -> None
node_count = l1.countnodes()
print(f"Number of nodes in the linked list: {node_count}")  # Output: Number of nodes in the linked list: 3
# time complexity of countnodes is O(n) where n is the number of nodes in the linked list
# space complexity is O(1) as we are using constant space for the count variable