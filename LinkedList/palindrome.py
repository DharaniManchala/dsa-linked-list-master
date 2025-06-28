class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        def reverse_list(node):
            prev=None
            while node:
                newnode=node.next
                node.next=prev
                prev=node
                node=newnode
            return prev
        second_half=reverse_list(slow)
        first_half=self.head
        while second_half:
            if first_half.data!=second_half.data:
                return False
            first_half=first_half.next
            second_half=second_half.next
        return True
    def printList(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(2)
fourth = Node(1)
l1.head.next = second
second.next = third
third.next = fourth
l1.printList()
if l1.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
# time complexity-O(n)
# space complexity-O(1)