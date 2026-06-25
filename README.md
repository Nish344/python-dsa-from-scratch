# Python Data Structures & Algorithms from Scratch

A collection of core data structures and algorithms implemented entirely from scratch in Python, without relying on high-level built-in abstractions.

This repository serves as a structured initiative to bridge the gap to intermediate engineering by focusing on memory management, time complexity, and low-level mechanics.

## Repository Structure

* [Dynamic Array](./Arrays/dynamic_array.py) - A C-style contiguous memory array built using `ctypes`.
* [Singly Linked List](./Linked_Lists/linked_lists.py) - Pointer-based list with head insertion and traversal.
* [Queue](./Queues/queues_using_linked_lists.py) - FIFO queue backed by a linked list.
* [Stack (Array)](./Stacks/stacks_using_arrays.py) - Fixed-capacity LIFO stack using a Python list.
* [Stack (Linked List)](./Stacks/stacks_using_linked_lists.py) - Dynamic LIFO stack with string reversal and undo/redo demos.

## How to Run

Each data structure module includes an interactive Command Line Interface (CLI) for real-time testing.

Clone the repository and run the specific module directly:

```bash
git clone https://github.com/Nish344/python-dsa-from-scratch.git
cd python-dsa-from-scratch
python3 Arrays/dynamic_array.py
python3 Linked_Lists/linked_lists.py
python3 Queues/queues_using_linked_lists.py
python3 Stacks/stacks_using_arrays.py
python3 Stacks/stacks_using_linked_lists.py
```
