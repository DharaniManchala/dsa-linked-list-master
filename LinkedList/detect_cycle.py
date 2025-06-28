# # done by Floyd's Cycle-Finding Algorithm
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def detect_cycle(self):
#         slow=self.head
#         fast=self.head

#         while fast and fast.next:
            
#             slow=slow.next
#             fast=fast.next.next
#             if slow==fast:
#                 return True
#         return False
#     def printList(self):
#         current=self.head
#         visited=set()
#         while current:

#            if id(current)in visited:

#              print("Cycle detected, cannot print the list.")
#              break
#            print(current.data, end=" -> ")
#            visited.add(id(current))
#            current = current.next
#         else:
#             print("None")
            
    
# l1 = LinkedList()
# l1.head = Node(10)
# second = Node(20)
# third = Node(30)
# fourth = Node(40)
# fifth = Node(50)
# sixth = Node(60)
# l1.head.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth
# fifth.next = sixth
# # Creating a cycle for testing
# sixth.next = third  # Cycle created here
# l1.printList()  # Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> None
# cycle_exists = l1.detect_cycle()
# print(f"Cycle exists: {cycle_exists}")  # Output: Cycle exists: True



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def printList(self):
        current = self.head
        visited = set()
        while current:
            if id(current) in visited:
                print(f"{current.data} -> ... (cycle detected)")
                break
            print(current.data, end=" -> ")
            visited.add(id(current))
            current = current.next
        else:
            print("None")

# Create Linked List with cycle
l1 = LinkedList()
l1.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)
sixth = Node(60)
l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = third  # Create cycle

# Safe print
l1.printList()

# Detect cycle
cycle_exists = l1.detect_cycle()
print(f"Cycle exists: {cycle_exists}")
# Output: Cycle exists: True
# Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> ... (cycle detected)
# Note: The printList method will not print the entire list if a cycle is detected.
# time complexity: O(n)
# space complexity: O(n)