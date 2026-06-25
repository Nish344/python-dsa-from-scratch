class Node:
    """A single node in the queue."""
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    """
    A FIFO queue implementation using a singly linked list.
    Maintains front and rear pointers for O(1) enqueue and dequeue.
    """
    def __init__(self):
        self.front = None
        self.rear = None
        self.n = 0

    def __len__(self):
        """Returns the number of elements in the queue (O(1))."""
        return self.n

    def enqueue(self, item):
        """Adds an item to the rear of the queue (O(1))."""
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.n += 1

    def dequeue(self):
        """Removes and returns the front item of the queue (O(1))."""
        if self.front is None:
            raise IndexError("dequeue from empty queue")

        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.n -= 1
        return item

    def size(self):
        """Returns the number of elements in the queue (O(1))."""
        return self.n

    def clear(self):
        """Empties the queue (O(1))."""
        self.front = None
        self.rear = None
        self.n = 0

    def is_empty(self):
        """Returns True if the queue has no elements (O(1))."""
        return self.front is None

    def traverse(self):
        """Prints all queue elements from front to rear (O(n))."""
        if self.front is None:
            print("Queue is Empty")
            return

        curr = self.front
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def __str__(self):
        """Returns queue elements as a string: [a, b, c]"""
        if self.front is None:
            return '[]'

        result = ''
        curr = self.front
        while curr is not None:
            result += str(curr.data) + ', '
            curr = curr.next

        return '[' + result[:-2] + ']'


def main():
    """Interactive CLI for the Linked List Queue."""
    q = Queue()
    print("=== Queue (Linked List) Interactive CLI ===")

    while True:
        print("\n" + "-"*35)
        print(f"Current Queue: {q}")
        print(f"Metrics -> Elements: {len(q)} | Empty: {q.is_empty()}")
        print("-" * 35)
        print("1. Enqueue item")
        print("2. Dequeue item")
        print("3. Traverse queue")
        print("4. Clear queue")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        try:
            if choice == '1':
                item = input("Enter item to enqueue: ")
                q.enqueue(item)
            elif choice == '2':
                dequeued = q.dequeue()
                print(f">> Successfully dequeued: {dequeued}")
            elif choice == '3':
                q.traverse()
            elif choice == '4':
                q.clear()
                print(">> Queue cleared.")
            elif choice == '5':
                print("Exiting CLI...")
                break
            else:
                print(">> Invalid choice. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f">> ERROR: {e}")


if __name__ == '__main__':
    main()
