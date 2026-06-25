class Node:
    """A single node in the stack."""
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    """
    A LIFO stack implementation using a singly linked list.
    The top pointer always references the most recently pushed node.
    """
    def __init__(self):
        self.top = None
        self.n = 0

    def __len__(self):
        """Returns the number of elements in the stack (O(1))."""
        return self.n

    def is_empty(self):
        """Returns True if the stack has no elements (O(1))."""
        return self.top is None

    def push(self, item):
        """Pushes an item onto the top of the stack (O(1))."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.n += 1

    def peek(self):
        """Returns the top item without removing it (O(1))."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def pop(self):
        """Removes and returns the top item of the stack (O(1))."""
        if self.is_empty():
            raise IndexError("pop from empty stack")

        data = self.top.data
        self.top = self.top.next
        self.n -= 1
        return data

    def traverse(self):
        """Prints all stack elements from top to bottom (O(n))."""
        if self.is_empty():
            print("Stack is Empty")
            return

        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def __str__(self):
        """Returns stack elements as a string from top to bottom."""
        if self.is_empty():
            return '[]'

        result = ''
        temp = self.top
        while temp is not None:
            result += str(temp.data) + ', '
            temp = temp.next

        return '[' + result[:-2] + ']'

    def string_reversal(self, text):
        """Reverses a string by pushing chars onto the stack and popping (O(n))."""
        for ch in text:
            self.push(ch)

        rev = ''
        while not self.is_empty():
            rev += self.pop()

        return rev

    def undo_redo(self, text, commands):
        """Simulates undo ('u') and redo ('r') operations on a string using two stacks."""
        new_stack = Stack()

        for ch in text:
            self.push(ch)

        for c in commands:
            if c == 'u':
                if not self.is_empty():
                    data = self.pop()
                    new_stack.push(data)
            elif c == 'r':
                if not new_stack.is_empty():
                    data = new_stack.pop()
                    self.push(data)

        res = ''
        while not self.is_empty():
            res += self.pop()

        print("The Final String is: " + res)


def main():
    """Interactive CLI for the Linked List Stack."""
    s = Stack()
    print("=== Stack (Linked List) Interactive CLI ===")

    while True:
        print("\n" + "-"*35)
        print(f"Current Stack: {s}")
        print(f"Metrics -> Elements: {len(s)} | Empty: {s.is_empty()}")
        print("-" * 35)
        print("1. Push item")
        print("2. Pop item")
        print("3. Peek top item")
        print("4. Traverse stack")
        print("5. Reverse a string")
        print("6. Undo/Redo demo")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

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
                text = input("Enter string to reverse: ")
                reversed_text = s.string_reversal(text)
                print(f">> Reversed string: {reversed_text}")
            elif choice == '6':
                text = input("Enter initial string: ")
                commands = input("Enter undo/redo commands (u/r): ")
                s.undo_redo(text, commands)
            elif choice == '7':
                print("Exiting CLI...")
                break
            else:
                print(">> Invalid choice. Please enter a number between 1 and 7.")
        except Exception as e:
            print(f">> ERROR: {e}")


if __name__ == '__main__':
    main()
