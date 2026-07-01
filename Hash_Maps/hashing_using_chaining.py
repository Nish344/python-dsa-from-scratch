class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    
    def insert_tail(self, key,value):
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
            self.n += 1
            return 
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        self.n += 1

    # def insert_after(self, target_value, new_value):
    #     """Inserts a new value immediately after the first occurrence of target_value (O(n))."""
    #     temp = self.head
        
    #     while temp is not None:
    #         if temp.value == target_value:
    #             new_node = Node(new_value)
    #             new_node.next = temp.next
    #             temp.next = new_node
    #             self.n += 1
    #             return
    #         temp = temp.next
            
    #     raise ValueError(f"Target value {target_value} not found in the list.")
            
    def delete_tail(self):
        """Removes the last node of the list (O(n))."""
        if self.head is None:
            raise IndexError("Cannot delete from an empty linked list.")
        
        if self.head.next is None:
            self.delete_head()
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        
        temp.next = None
        self.n -= 1

    def delete_value(self, value):
        """Removes the first node that matches the target value (O(n))."""
        if self.head is None:
            raise ValueError("List is empty.")

        if self.head.value == value:
            self.delete_head()
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.value == value:
                temp.next = temp.next.next
                self.n -= 1
                return
            temp = temp.next
            
        raise ValueError(f"Value {value} not found in list.")
    
    def search_value(self, key):
        """Returns the index of the first occurrence of the value (O(n))."""
        temp = self.head
        pos = 0

        while temp is not None:
            if temp.key == key:
                return pos 
            temp = temp.next
            pos += 1

        return -1

            
    def __getitem__(self, idx):
        """Retrieves the value at a specific index (O(n))."""
        if idx < 0:
            idx = self.n + idx

        if not (0 <= idx < self.n):
            raise IndexError("Index out of bounds")

        temp = self.head
        for _ in range(idx):
            temp = temp.next

        return temp.value

    def __str__(self):
        """Prints the linked list visually: 1 -> 2 -> 3"""
        if self.head is None:
            return "Empty Bucket"

        temp = self.head
        result = ''

        while temp is not None:
            result += str(temp.key) + ' --> ' + str(temp.value)
            temp = temp.next
        
        return result[:-4]
    
    def get_node_at_index(self,index):
        temp = self.head
        counter = 0

        for i in range(index):  
            if counter == index:
                return temp
            
            temp = temp.next
            counter += 1 

    
class Dictionary:
    def __init__(self,capacity):
        self.capacity = capacity
        self.n = 0
        self.buckets = self.make_array(self.capacity)

    def make_array(self,cap):
        L = []

        for i in range (cap):
            L.append(LinkedList())

        return L
    
    def put(self,key,value):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            self.buckets[bucket_index].insert_tail(key,value)
            self.size += 1

            if (self.size/self.capacity >= 2):
                self.rehash(    )
        else:
            node = self.buckets[node_index].get_node_at_index(node_index)
            node.value = value

    def get(self,key):
        bucekt_index = self.hash_function(key)

        res = self.buckets[bucekt_index].search_value(key)

        if res == -1:
            return -1
        else:
            node = self.buckets[bucekt_index].get_node_at_index(res)
            return node.value
        
    def __setitem__(self, key, value):
        pass

    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        bucket_index = self.hash_function(key)

        self.buckets[bucket_index].remove(key)


    def rehash(self):
        self.capacity = self.capacity * 2
        old_buckets = self.buckets
        self.size = 0
        self.buckets = self.make_array(self.capacity)

        for i in old_buckets:
            for j in range(old_buckets[i].n):
                node = i.get_node_at_index(j)
                self.put(node.key,node.value)




    def get_node_index(self,bucket_index,key):
        node_index = self.buckets[bucket_index].search_value(key)
        return node_index
 
    def hash_function(self,key):
        return abs(hash(key)) % self.capacity