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
    
    def search_value(self, value):
        """Returns the index of the first occurrence of the value (O(n))."""
        temp = self.head
        pos = 0

        while temp is not None:
            if temp.value == value:
                return pos 
            temp = temp.next
            pos += 1

        return -1

    def replace_max_value(self, item):
        """Replaces the value of the node holding the maximum value (O(n))."""
        if self.head is None:
            raise ValueError("List is empty.")

        temp = self.head
        max_value = temp

        while temp is not None:
            if temp.value > max_value.value:
                max_value = temp
            temp = temp.next

        max_value.value = item

    def reverse_list(self):
        """Reverses the list by building a new list and reassigning the head (O(n))."""
        new_list = LinkedList()
        temp = self.head

        while temp is not None:
            new_list.insert_head(temp.value)
            temp = temp.next
        
        self.head = new_list.head
        self.n = new_list.n

    def reverse_inplace(self):
        """Reverses the list in-place by reversing node pointers (O(n))."""
        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            
            prev_node = curr_node
            curr_node = next_node
        
        self.head = prev_node
            
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
            return "Empty List"

        temp = self.head
        result = ''

        while temp is not None:
            result += str(temp.value) + ' -> '
            temp = temp.next
        
        return result[:-4]


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
        print("7. Search by Value")
        print("8. Reverse List (new list)")
        print("9. Reverse In-Place")
        print("10. Replace Max Value")
        print("11. Clear List")
        print("12. Exit")
        
        choice = input("\nEnter your choice (1-12): ")
        
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
                val = input("Enter value to search: ")
                pos = ll.search_value(val)
                if pos != -1:
                    print(f">> Value found at index {pos}.")
                else:
                    print(">> Value not found.")
            elif choice == '8':
                ll.reverse_list()
                print(">> List reversed (new list).")
            elif choice == '9':
                ll.reverse_inplace()
                print(">> List reversed in-place.")
            elif choice == '10':
                item = input("Enter replacement value for max node: ")
                ll.replace_max_value(item)
                print(">> Max value replaced.")
            elif choice == '11':
                ll.clear()
                print(">> List cleared.")
            elif choice == '12':
                print("Exiting CLI...")
                break
            else:
                print(">> Invalid choice. Please enter a number between 1 and 12.")
        except Exception as e:
            print(f">> ERROR: {e}")


if __name__ == "__main__":
    main()
