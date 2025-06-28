class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def merge(self,l1,l2):
        dummy=Node(0)
        current=dummy
        while l1 and l2:
            if l1.data<l2.data:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
            if l1:
                current.next=l1
            if l2:
                current.next=l2
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
l2=LinkedList()
l2.head=Node(15)
second2=Node(25)
third2=Node(35)
l2.head.next=second2
second2.next=third2
l1.printList()
l2.printList()
l3=LinkedList()
l3.merge(l1.head,l2.head)
l3.printList()
# time complexity-O(n)
# space complexity-O(1)
# Note: This implementation assumes that the input linked lists are already sorted.