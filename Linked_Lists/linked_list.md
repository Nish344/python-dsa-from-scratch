# Singly Linked List

A fundamental pointer-based data structure implemented from scratch in Python. Unlike dynamic arrays which rely on contiguous memory, linked lists use dynamically allocated nodes scattered across memory, connected via object references (pointers).

## 🧠 Core Concept
The list maintains a reference to the `head` (the first node). Every node contains a `value` and a `next` pointer pointing to the subsequent node. Traversal is strictly sequential (O(n)), but insertions and deletions at the head are incredibly fast (O(1)) because no memory shifting is required.

## ⏱️ Time Complexity

| Operation | Time Complexity | Note |
| :--- | :--- | :--- |
| **Insert Head** | O(1) | Pointer reassignment only. |
| **Insert Tail** | O(n) | Requires traversing the entire list. |
| **Delete Head** | O(1) | Pointer reassignment only. |
| **Delete Tail** | O(n) | Requires traversal to find the second-to-last node. |
| **Search / Access** | O(n) | Sequential traversal required. |

## 🏗️ Implementation Details
* **Node Class:** A separate helper class handles the individual data structures.
* **State Management:** Maintains a discrete `self.n` variable to track list length in O(1) time without requiring a full traversal for `len()`.
* **Garbage Collection:** Deleting nodes is handled implicitly by Python's garbage collector once the `next` reference is removed or bypassed.

## Upcoming Features
This module will be expanded with the following operations:
* `find_middle()` - Using the fast/slow pointer (tortoise and hare) algorithm.
* Detection of cyclic loops.