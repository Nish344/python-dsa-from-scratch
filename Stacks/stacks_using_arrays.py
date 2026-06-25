class Stack:
    """
    A LIFO stack implementation using a fixed-size array.
    Tracks the top index to manage push and pop operations.
    """
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def __len__(self):
        """Returns the number of elements in the stack (O(1))."""
        return self.top + 1

    def push(self, item):
        """Pushes an item onto the top of the stack (O(1))."""
        if self.top == self.size - 1:
            raise OverflowError("Stack overflow")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        """Removes and returns the top item of the stack (O(1))."""
        if self.top == -1:
            raise IndexError("pop from empty stack")

        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        """Returns the top item without removing it (O(1))."""
        if self.top == -1:
            raise IndexError("peek from empty stack")
        return self.stack[self.top]

    def is_empty(self):
        """Returns True if the stack has no elements (O(1))."""
        return self.top == -1

    def traverse(self):
        """Prints all stack elements from bottom to top (O(n))."""
        if self.top == -1:
            print("Stack is Empty")
            return

        for i in range(self.top + 1):
            print(self.stack[i])

    def __str__(self):
        """Returns stack elements as a string: [a, b, c]"""
        if self.top == -1:
            return '[]'

        result = ''
        for i in range(self.top + 1):
            result += str(self.stack[i]) + ', '

        return '[' + result[:-2] + ']'


def main():
    """Interactive CLI for the Array-based Stack."""
    try:
        capacity = int(input("Enter stack capacity: "))
    except ValueError:
        print("Invalid capacity. Using default of 10.")
        capacity = 10

    s = Stack(capacity)
    print("=== Stack (Array) Interactive CLI ===")

    while True:
        print("\n" + "-"*35)
        print(f"Current Stack: {s}")
        print(f"Metrics -> Capacity: {s.size} | Elements: {len(s)}")
        print("-" * 35)
        print("1. Push item")
        print("2. Pop item")
        print("3. Peek top item")
        print("4. Traverse stack")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        try:
            if choice == '1':
                item = input("Enter item to push: ")
                s.push(item)
            elif choice == '2':
                popped = s.pop()
                print(f">> Successfully popped: {popped}")
            elif choice == '3':
                print(f">> Top item: {s.peek()}")
            elif choice == '4':
                s.traverse()
            elif choice == '5':
                print("Exiting CLI...")
                break
            else:
                print(">> Invalid choice. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f">> ERROR: {e}")


if __name__ == '__main__':
    main()
