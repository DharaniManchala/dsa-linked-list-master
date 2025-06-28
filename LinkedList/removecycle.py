class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def remove_cycle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return   # No cycle detected
        prev=None
        slow=self.head
        while slow!=fast:
            prev=fast
            slow=slow.next
            fast=fast.next
        prev.next=None
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
# Example usage
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
# Creating a cycle for testing
sixth.next = third  # Cycle created here
l1.printList()  # Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> None
l1.remove_cycle()
l1.printList()  # Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> None
# time complexity: O(n)
# space complexity: O(1)
