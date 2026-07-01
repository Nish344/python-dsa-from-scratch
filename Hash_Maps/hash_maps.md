# Hash Map (Linear Probing)

A key-value dictionary implemented from scratch using **open addressing** with **linear probing** for collision resolution.

## Core Concept
Each key is mapped to an index via `abs(hash(key)) % size`. When that slot is occupied by a different key, the table probes the next index until an empty slot or a matching key is found. Keys and values are stored in parallel arrays: `slots` for keys and `data` for values.

## ⏱️ Time Complexity

| Operation | Average Case | Worst Case | Note |
| :--- | :--- | :--- | :--- |
| **Put / Update** | O(1) | O(n) | Worst case when table is crowded. |
| **Get** | O(1) | O(n) | Linear probe on collision. |
| **Contains** | O(1) | O(n) | Uses `get` internally. |
| **Clear** | O(n) | O(n) | Resets both arrays. |

## Implementation Details
* **Collision Resolution:** Linear probing — on collision, move to `(index + 1) % size`.
* **State Management:** `self.n` tracks the number of entries for O(1) `len()`.
* **Error Handling:** Raises `KeyError` for missing keys and `OverflowError` when the table is full.
* **Dunder Methods:** Implements `__len__`, `__getitem__`, `__setitem__`, `__contains__`, and `__str__`.

## Upcoming Features
* Delete with tombstone markers.
* Dynamic resizing when load factor exceeds a threshold.
* Separate chaining variant using linked lists.
