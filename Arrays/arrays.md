# Dynamic Array

A low-level implementation of a Python dynamic list. Standard Python `list` objects are dynamic arrays under the hood. This implementation recreates that behavior using a C-style array via the `ctypes` module.

## Core Concept
This dynamic array manages a contiguous block of memory. When the number of elements reaches the allocated capacity, the array triggers a **geometric resize** (doubling in size). It allocates a new, larger block of memory, copies the existing elements over, and reassigns the main pointer.

## ⏱️ Time Complexity

| Operation | Best Case | Worst Case | Amortized |
| :--- | :--- | :--- | :--- |
| **Access / Indexing** | O(1) | O(1) | O(1) |
| **Append** | O(1) | O(n) *(if resizing)* | O(1) |
| **Insert (at index)** | O(n) | O(n) | O(n) |
| **Pop (last item)** | O(1) | O(1) | O(1) |
| **Delete (by index)** | O(n) | O(n) | O(n) |

##  Implementation Details
* **Memory Allocation:** Handled via `ctypes.py_object` to create raw pointer arrays.
* **Name Mangling:** Internal helper methods like `__resize` and `__make_array` use double leading underscores to protect the internal API.
* **Dunder Methods:** Implements `__len__`, `__getitem__`, `__delitem__`, and `__str__` to allow standard Python syntax (e.g., `arr[0]`, `len(arr)`, `print(arr)`).

## Upcoming Features
This module is actively being expanded. The following functions are scheduled to be implemented next:
* `sort()` - In-place sorting algorithms (e.g., Quicksort or Merge Sort).
* `max()` / `min()` - Linear scans to return boundary values.
* `extend()` - Appending multiple items from another iterable.
