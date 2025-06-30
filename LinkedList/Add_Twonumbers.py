class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_two_numbers(self,l1,l2):
        dummy=Node(0)
        tail=dummy
        carry=0
        while l1 or l2 or carry:
            v1=l1.data if l1 else 0
            v2=l2.data if l2 else 0
            total=v1+v2+carry
            carry=total//10
            digit=total%10
            tail.next=Node(digit)
            tail=tail.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
    def printList(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
l1 = LinkedList()
l1.head = Node(2)
second = Node(4)
third = Node(3)
l1.head.next = second
second.next = third
l2 = LinkedList()
l2.head = Node(5)
second = Node(6)
third = Node(4)
l2.head.next = second
second.next = third
result = LinkedList()
result.head = result.add_two_numbers(l1.head, l2.head)
result.printList()
# Output: 7->0->8->None
# # Time complexity: O(max(m, n)), where m and n are the lengths of the two linked lists.
# # Space complexity: O(max(m, n)), for the result linked list.

    