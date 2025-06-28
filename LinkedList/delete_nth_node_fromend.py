class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def delete_nth_node_fromend(self,n):
        dummy=Node(0)
        dummy.next=self.head
        slow=fast=dummy
        for _ in range(n):
            if fast.next is None:
                print("n is larger than length of the list")
                return 
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        self.head=dummy.next
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
fourth=Node(40)
fifth=Node(50)
l1.head.next=second
second.next=third
third.next=fourth
fourth.next=fifth
l1.printList()
l1.delete_nth_node_fromend(2)
l1.printList()
# time complexity-O(n)
# space complexity-O(1)