class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
l1=Linkedlist()
l1.head=Node(10)
second=Node(20)
third=Node(30)
l1.head.next=second
second.next=third
l1.printList()  # Output: 10 -> 20 -> 30 -> None
l1.insert_at_begin(5)
l1.printList()  # Output: 5 -> 10 -> 20 -> 30 -> None
# time complexity of insert_at_begin is O(1) as we are inserting at the beginning
# space complexity is O(1) as we are using constant space for the new_node pointer