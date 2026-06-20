import ctypes

class DynamicArray:
    """
    A custom dynamic array implementation in Python simulating the built-in list.
    Manages low-level memory allocation and dynamic resizing.
    """
    def __init__(self):
        self.size = 1     # Total allocated memory capacity
        self.n = 0        # Number of elements currently stored
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        """Creates a new C-style array with the given capacity."""
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        """Returns the number of elements in the array (O(1))."""
        return self.n
    
    def append(self, item):
        """Adds an item to the end of the array (Amortized O(1))."""
        # Trigger geometric resize if capacity is reached
        if self.size == self.n:
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n += 1

    def pop(self):
        """Removes and returns the last item in the array (O(1))."""
        if self.n == 0:
            raise IndexError("pop from empty array")
        
        self.n -= 1
        return self.A[self.n]
        
    def clear(self):
        """Empties the array and resets capacity."""
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size) # Wipes the slate clean in memory
        
    def find(self, item):
        """Returns the index of the first occurrence of the item (O(n))."""
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return -1 # Standard convention to return -1 if item is not found

    def __resize(self, new_capacity):
        """Allocates a new array with new_capacity and copies elements (O(n))."""
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # Copy existing elements over to the newly allocated block
        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B # Reassign the main pointer to the new array

    def __getitem__(self, key):
        """Allows bracket indexing, e.g., arr[0] and negative indexing arr[-1] (O(1))."""
        # Support for negative indexing (e.g., -1 gets the last item)
        if key < 0:
            key = self.n + key 

        # Check bounds using strictly less than self.n
        if 0 <= key < self.n:
            return self.A[key]
        else:
            raise IndexError("Index out of bounds")
        
    def __delitem__(self, pos):
        """Deletes an item at a specific index and shifts elements left (O(n))."""
        if not (0 <= pos < self.n):
            raise IndexError("Index out of bounds")

        for i in range(pos, self.n - 1):
            self.A[i] = self.A[i+1]
        self.n -= 1

    def insert(self, pos, item):
        """Inserts an item at a specific index and shifts elements right (O(n))."""
        if not (0 <= pos <= self.n):
            raise IndexError("Index out of bounds")

        if self.n == self.size:
            self.__resize(self.size * 2)
        
        # Shift elements right to make room for the new item
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n += 1

    def remove(self, item):
        """Removes the first occurrence of an item by value (O(n))."""
        pos = self.find(item)
        if pos != -1:
            self.__delitem__(pos)
        else: 
            raise ValueError(f"list.remove(x): x not in list")
        
    def __str__(self):
        """Prints the array in standard Python list format: [a, b, c]"""
        if self.n == 0:
            return '[]'
        
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ', '
            
        # Slice off the trailing comma and space before closing the bracket
        return '[' + result[:-2] + ']'


def main():
    """Command Line Interface to interactively test the DynamicArray."""
    arr = DynamicArray()
    print("=== Dynamic Array Interactive CLI ===")
    print("Built from scratch using ctypes.")
    
    while True:
        print("\n" + "-"*35)
        print(f"Current Array: {arr}")
        print(f"Metrics -> Capacity: {arr.size} | Elements: {len(arr)}")
        print("-" * 35)
        print("1. Append item")
        print("2. Pop item")
        print("3. Insert item at index")
        print("4. Remove item by value")
        print("5. Clear array")
        print("6. Get item at index")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        try:
            if choice == '1':
                item = input("Enter item to append: ")
                arr.append(item)
            elif choice == '2':
                popped = arr.pop()
                print(f">> Successfully popped: {popped}")
            elif choice == '3':
                pos = int(input("Enter index to insert at: "))
                item = input("Enter item to insert: ")
                arr.insert(pos, item)
            elif choice == '4':
                item = input("Enter item to remove: ")
                arr.remove(item)
            elif choice == '5':
                arr.clear()
                print(">> Array cleared.")
            elif choice == '6':
                pos = int(input("Enter index to fetch: "))
                print(f">> Item at index {pos}: {arr[pos]}")
            elif choice == '7':
                print("Exiting CLI...")
                break
            else:
                print(">> Invalid choice. Please enter a number between 1 and 7.")
        except Exception as e:
            # Catches custom IndexErrors and ValueErrors cleanly
            print(f">> ERROR: {e}")

if __name__ == "__main__":
    main()