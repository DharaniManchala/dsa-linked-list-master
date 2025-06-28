class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def intersection(head1,head2):
        def get_length(head):
            length=0
            while head:
                length+=1
                head=head.next
            return length
        len1=get_length(head1)
        len2=get_length(head2)
        diff=abs(len1-len2)
        if len1>len2:
            for _ in range(diff):
                head1=head1.next
        else:
            for _ in range(diff):
                head2=head2.next
        while head1 and head2:
            if head1==head2:
                return head1
            head1=head1.next
            head2=head2.next
        return None
    def printList(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
shared=Node(6)
shared.next=Node(7)
l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(3)

l1.head.next = second
second.next = third
third.next = shared
# l1.head.next.next.next = fifth  # Creating a linked list: 1->2->3->4->5
l2 = LinkedList()
l2.head = Node(4)
second2 = Node(5)

l2.head.next = second2
second2.next = shared
# third2.next = fourth2  # Creating a linked list: 6->7->8->4->5
intersection_node = LinkedList.intersection(l1.head, l2.head)
if intersection_node:
    print(f"The intersection node is: {intersection_node.data}")
else:
    print("There is no intersection between the two linked lists.")
# timecomplexity-O(m+n)
# space complexity-O(1)