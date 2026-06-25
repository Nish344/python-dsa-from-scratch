# Stack

LIFO (Last-In-First-Out) stack implementations from scratch in two variants: a fixed-size array and a singly linked list.

## Core Concept
The most recently pushed element is always the first one removed. The array variant uses a `top` index into a pre-allocated list; the linked-list variant uses a `top` pointer to the head node.

## ⏱️ Time Complexity

| Operation | Array Stack | Linked List Stack |
| :--- | :--- | :--- |
| **Push** | O(1) | O(1) |
| **Pop** | O(1) | O(1) |
| **Peek** | O(1) | O(1) |
| **Traverse** | O(n) | O(n) |

## Implementation Details

### Array Stack (`stacks_using_arrays.py`)
* Fixed capacity set at construction time.
* Raises `OverflowError` on push when full, `IndexError` on pop/peek when empty.

### Linked List Stack (`stacks_using_linked_lists.py`)
* Dynamic size — no capacity limit.
* Includes `string_reversal()` and `undo_redo()` demos that showcase classic stack use cases.
* Maintains `self.n` for O(1) length tracking.

## Upcoming Features
* Balanced parentheses checker.
* Expression evaluation using two stacks.
