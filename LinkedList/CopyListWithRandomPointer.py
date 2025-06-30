# Copy a linked list with random pointers
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

class LinkedList:
    def __init__(self):
        self.head = None

    def copyListWithRandomPointer(self, head):
        if not head:
            return None

        # Step 1: Insert copied nodes after each original node
        current = head
        while current:
            newnode = Node(current.data)
            newnode.next = current.next
            current.next = newnode
            current = newnode.next

        # Step 2: Assign random pointers to copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the copied list from the original
        original = head
        copy = head.next
        copy_head = copy
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return copy_head

    # Print any linked list given its head
    def printList(self, head):
        current = head
        while current:
            random_data = current.random.data if current.random else None
            print(f"Node data: {current.data}, Random data: {random_data}")
            current = current.next

# 🔄 Create original list
l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(3)

l1.head.next = second
second.next = third

# Set up random pointers
l1.head.random = second     # Node 1 → Random → Node 2
second.random = l1.head     # Node 2 → Random → Node 1
third.random = second       # Node 3 → Random → Node 2

# 🧬 Deep Copy the list
copied_head = l1.copyListWithRandomPointer(l1.head)

# 🖨️ Print the copied list
print("Copied Linked List:")
l1.printList(copied_head)
#⏱️ Time Complexity: O(n)
# Reason: We traverse the linked list 3 times:

# To insert copied nodes

# To update random pointers

# To separate the copied list

# Each traversal is O(n) where n is the number of nodes.


# 💾 Space Complexity:
# Auxiliary Space: O(1)

# We do not use extra data structures like a hashmap.

# Overall Space: O(n)

# Because we create a new list with n nodes.


