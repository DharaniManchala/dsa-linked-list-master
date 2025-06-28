class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def delete_by_value(self,value):
        current=self.head
        if current and current.data==value:
            self.head=current.next
            return
        # node is somewhwere else
        prev=None
        while current and current.data!=value:
            prev=current
            current=current.next
        if current is None:
            print(f"{value}not found")
            return 
        prev.next=current.next
    def printList(self):
        current=self.head
        while(current):
            print(current.data,end="->")
            current=current.next
        print("None")
l1=LinkedList()
l1.head=Node(10)
second=Node(20)
third=Node(30)
l1.head.next=second
second.next=third
l1.printList()
l1.delete_by_value(20)
l1.printList()
# timecomplexity-O(n)
# space complexity-O(1)

