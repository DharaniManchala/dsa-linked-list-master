class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class LRU_Cache:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    def insert_at_front(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    def get(self,key:int)->int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert_at_front(node)
            return node.value
        return -1
    def put(self,key:int,value:int)->None:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
        newnode=Node(key,value)
        self.insert_at_front(newnode)
        self.cache[key]=newnode
        if len(self.cache)>self.capacity:
            lru=self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
      # Debug print
    def print_cache(self):
        print("Current Cache State (Most Recent -> Least):")
        curr = self.head.next
        while curr != self.tail:
            print(f"[{curr.key}:{curr.value}]", end=" <-> ")
            curr = curr.next
        print("None")

# 🔄 Testing the LRU Cache
lru = LRU_Cache(2)       # Capacity = 2
lru.put(1, 100)         # Cache: 1
lru.put(2, 200)         # Cache: 2 <-> 1
lru.print_cache()
print("Get(1):", lru.get(1))  # Should return 100
lru.print_cache()
lru.put(3, 300)         # Evicts key 2 (LRU), adds 3
lru.print_cache()
print("Get(2):", lru.get(2))  # 

        
        
     

        
        
        
       


    