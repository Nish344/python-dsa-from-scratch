class Node:
    """A single node in the linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A Singly Linked List implementation."""
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        """Returns the number of nodes in the list (O(1))."""
        return self.n
    
    def insert_head(self, value):
        """Inserts a new node at the beginning of the list (O(1))."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1
    
    def insert_tail(self, value):
        """Inserts a new node at the end of the list (O(n))."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.n += 1
            return 
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        self.n += 1

    def insert_after(self, target_value, new_value):
        """Inserts a new value immediately after the first occurrence of target_value (O(n))."""
        temp = self.head
        
        while temp is not None:
            if temp.value == target_value:
                new_node = Node(new_value)
                new_node.next = temp.next
                temp.next = new_node
                self.n += 1
                return
            temp = temp.next
            
        raise ValueError(f"Target value {target_value} not found in the list.")
        
    def clear(self):
        """Empties the list by removing the head reference (O(1))."""
        self.head = None
        self.n = 0
        
    def delete_head(self):
        """Removes the first node of the list (O(1))."""
        if self.head is None:
            raise IndexError("Cannot delete from an empty linked list.")
        
        self.head = self.head.next
        self.n -= 1

    def delete_tail(self):
        """Removes the last node of the list (O(n))."""
        if self.head is None:
            raise IndexError("Cannot delete from an empty linked list.")
        
        # If there's only one node
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

        # If the head is the target value
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
    
    def search_value(self, value):
        """Returns the index of the first occurrence of the value (O(n))."""
        temp = self.head
        pos = 0

        while temp is not None:
            if temp.value == value:
                return pos 
            temp = temp.next
            pos += 1

        return -1 # Standard convention for 'not found'
            
    def __getitem__(self, idx):
        """Retrieves the value at a specific index (O(n))."""
        if not (0 <= idx < self.n):
            raise IndexError("Index out of bounds")

        temp = self.head
        for _ in range(idx):
            temp = temp.next

        return temp.value

    def __str__(self):
        """Prints the linked list visually: 1 -> 2 -> 3"""
        if self.head is None:
            return "Empty List"

        temp = self.head
        result = ''

        while temp is not None:
            result += str(temp.value) + ' -> '
            temp = temp.next
        
        return result[:-4] # Slices off the final ' -> '


def main():
    """Interactive CLI for the Linked List."""
    ll = LinkedList()
    print("=== Linked List Interactive CLI ===")
    
    while True:
        print("\n" + "-"*40)
        print(f"Current List: {ll}")
        print(f"Metrics -> Total Nodes: {len(ll)}")
        print("-" * 40)
        print("1. Insert at Head")
        print("2. Insert at Tail")
        print("3. Insert after specific value")
        print("4. Delete Head")
        print("5. Delete Tail")
        print("6. Delete by Value")
        print("7. Clear List")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        try:
            if choice == '1':
                val = input("Enter value to insert at head: ")
                ll.insert_head(val)
            elif choice == '2':
                val = input("Enter value to insert at tail: ")
                ll.insert_tail(val)
            elif choice == '3':
                target = input("Enter target value to insert after: ")
                val = input("Enter new value to insert: ")
                ll.insert_after(target, val)
            elif choice == '4':
                ll.delete_head()
                print(">> Head deleted.")
            elif choice == '5':
                ll.delete_tail()
                print(">> Tail deleted.")
            elif choice == '6':
                val = input("Enter value to delete: ")
                ll.delete_value(val)
                print(f">> Value {val} deleted.")
            elif choice == '7':
                ll.clear()
                print(">> List cleared.")
            elif choice == '8':
                print("Exiting CLI...")
                break
            else:
                print(">> Invalid choice.")
        except Exception as e:
            print(f">> ERROR: {e}")

if __name__ == "__main__":
    main()