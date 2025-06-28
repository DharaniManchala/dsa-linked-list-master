class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        return False
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
print(l1.search(20))  # Output: True
print(l1.search(40))  # Output: False
# time complexity of search is O(n) where n is the number of nodes in the linked list
# space complexity is O(1) as we are using constant space for the current pointer
    
