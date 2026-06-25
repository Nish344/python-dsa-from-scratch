# Queue (Linked List)

A First-In-First-Out (FIFO) queue implemented from scratch using a singly linked list. Maintains explicit `front` and `rear` pointers so enqueue and dequeue happen at opposite ends without shifting elements.

## Core Concept
New items are appended at the `rear`; removals always happen at the `front`. A discrete `self.n` counter tracks length in O(1) time without traversing the list.

## ⏱️ Time Complexity

| Operation | Time Complexity | Note |
| :--- | :--- | :--- |
| **Enqueue** | O(1) | Append at rear pointer. |
| **Dequeue** | O(1) | Remove at front pointer. |
| **Peek / Access** | O(1) | Front node is directly reachable. |
| **Size / Length** | O(1) | Maintained via `self.n`. |
| **Traverse** | O(n) | Sequential walk from front to rear. |

## Implementation Details
* **Node Class:** Each node stores `data` and a `next` pointer.
* **Empty Queue Handling:** Both `front` and `rear` are set to `None` when the last element is dequeued.
* **Dunder Methods:** Implements `__len__` and `__str__` for standard Python syntax.

## Upcoming Features
* Circular queue variant using a fixed-size array.
* Priority queue implementation.
