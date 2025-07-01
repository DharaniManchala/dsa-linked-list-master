# # Recursive approach to flatten a multilevel doubly linked list
# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
#         self.prev=None
#         self.child=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def flatten(self,head):
#         if not head:
#             return head
#         current=head
#         while current:
#             if current.child:
#                 nextnode=current.next
#                 child=self.flatten(current.child)
#                 current.next=child
#                 child.prev=current
#                 current.child=None
#                 temp=child
#                 while temp.next:
#                     temp=temp.next
#                 temp.next=nextnode
#                 if nextnode:
#                     nextnode.prev=temp
#                 current=nextnode
#             else:
#                 current=current.next
#         return head
#     def printList(self,head):
#         current=head
#         while current:
#             print(current.val,end="<->")
#             current=current.next
#         print("None")
# # Create nodes manually to form a multilevel list
# head = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)

# # First level
# head.next = node2
# node2.prev = head
# node2.next = node3
# node3.prev = node2

# # Child level
# child1 = Node(7)
# child2 = Node(8)
# child3 = Node(9)

# node3.child = child1
# child1.next = child2
# child2.prev = child1
# child2.next = child3
# child3.prev = child2

# # Add more after main list
# node3.next = node4
# node4.prev = node3
# node4.next = node5
# node5.prev = node4
# node5.next = node6
# node6.prev = node5

# # Now flatten and print
# ll = LinkedList()
# flattened_head = ll.flatten(head)
# ll.printList(flattened_head)

# O(n) — Every node is visited once

# Space: O(depth) — Recursive call stack


# iterative approach with stack
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None

class LinkedList:
    def __init__(self):
        self.head = None

    def flatten(self, head):
        if not head:
            return None

        stack = []
        current = head

        while current:
            if current.child:
                if current.next:
                    stack.append(current.next)  # Save next node for later

                current.next = current.child
                current.child.prev = current
                current.child = None

            if not current.next and stack:
                temp = stack.pop()
                current.next = temp
                temp.prev = current

            current = current.next

        return head

    def printList(self, head):
        current = head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")

# Creating nodes for multilevel doubly linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

child1 = Node(5)
child2 = Node(6)

# Main level
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

# Child level
node2.child = child1
child1.next = child2
child2.prev = child1

# Flatten and print
ll = LinkedList()
flattened_head = ll.flatten(head)
ll.printList(flattened_head)


# 🕒 Time and Space Complexity:
# Time: O(n) — we visit each node once.

# Space: O(n) — for the stack in the worst case (deep nesting).


