class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseKGroup(self, head, k):
        # Check if there are at least k nodes to reverse
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            return head  # Not enough nodes to reverse

        # Reverse k nodes
        prev = None
        current = head
        next_node = None
        count = 0

        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1

        # Recur for the next group
        if next_node:
            head.next = self.reverseKGroup(next_node, k)

        return prev

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 🔄 Testing
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

print("Original list:")
ll.printList()

k = 2
ll.head = ll.reverseKGroup(ll.head, k)

print(f"\nList after reversing in k={k} groups:")
ll.printList()
# ➡️ Time: O(n)
# ➡️ Space: O(1) (iterative version)