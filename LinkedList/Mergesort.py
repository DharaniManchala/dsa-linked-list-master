class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def merge_sort(self,head):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.merge_sort(head)
        right=self.merge_sort(mid)
        return self.merge(left,right)
    def merge(self,l1,l2):
        dummy=Node(0)
        tail=dummy
        while l1 and l2:
            if l1.data<l2.data:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        tail.next=l1 if l1 else l2
        return dummy.next
    def sort(self):
        self.head=self.merge_sort(self.head)
    def printList(self):
        current=self.head
        while current:
            print(current.data, end="->")
            current=current.next
        print("None")
l1=LinkedList()
l1.head=Node(40)
second=Node(10)
third=Node(30)
fourth=Node(20)
fifth=Node(50)
l1.head.next=second
second.next=third
third.next=fourth
fourth.next=fifth
l1.printList()
l1.sort()
l1.printList()
# time complexity-O(n log n)
# space complexity-O(1) for linked list merge sort
# but O(n) for the recursive stack space


