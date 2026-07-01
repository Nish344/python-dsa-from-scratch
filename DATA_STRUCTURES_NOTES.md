# Complete Data Structures Notes

> **Scope:** Arrays, Linked Lists, Queues, Stacks, and Hash Maps.

---

## Table of Contents

1. [Arrays (Dynamic Array)](#1-arrays-dynamic-array)
2. [Linked Lists (Singly Linked List)](#2-linked-lists-singly-linked-list)
3. [Queues (FIFO)](#3-queues-fifo)
4. [Stacks (LIFO)](#4-stacks-lifo)
5. [Hash Maps](#5-hash-maps)
6. [Quick Comparison Cheat Sheet](#6-quick-comparison-cheat-sheet)

---

# 1. Arrays (Dynamic Array)

## 1.1 Introduction

An **array** is a collection of elements stored in **contiguous memory** — each item sits right next to the previous one in RAM, like books on a shelf numbered 0, 1, 2, …

A **dynamic array** (like Python's built-in `list`) starts small and **grows automatically** when full. The version in `Arrays/dynamic_array.py` uses `ctypes` to simulate raw C-style memory allocation.

```
Memory layout (capacity = 8, n = 5 elements):

Index:     [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]
         ┌────┬────┬────┬────┬────┬────┬────┬────┐
Values:  │ 10 │ 20 │ 30 │ 40 │ 50 │ -- │ -- │ -- │
         └────┴────┴────┴────┴────┴────┴────┴────┘
                              ↑
                         n = 5 (used)
                         size = 8 (capacity)
```

### Key Variables

| Variable | Meaning |
|----------|---------|
| `self.A` | Pointer to the underlying C-style array |
| `self.n` | Number of elements currently stored |
| `self.size` | Total allocated capacity |

---

## 1.2 Real-Life Analogy

Think of a **parking lot with numbered slots**:

- Any slot can be reached directly by number (random access).
- If all slots are full, the lot doubles in size and every car is moved to the new lot (resize).
- Inserting a car in the middle means shifting every car behind it forward — slow!

---

## 1.3 Merits & Demerits

| ✅ Merits | ❌ Demerits |
|-----------|-------------|
| **O(1) random access** by index | **O(n) insert/delete** in the middle |
| **Cache-friendly** — contiguous memory is fast for CPUs | **Resize cost** — occasional O(n) copy when capacity doubles |
| **Simple mental model** — just an indexed sequence | **Wasted space** — capacity may exceed actual elements |
| **Amortized O(1) append** at the end | Fixed overhead for small arrays |

---

## 1.4 Real-Life Examples

| Use Case | Why Arrays? |
|----------|-------------|
| **Image pixels** | Each pixel at `(row, col)` maps to a flat index |
| **Game leaderboards** | Sorted scores stored sequentially; fast index access |
| **Audio samples** | Sound wave amplitudes in a continuous buffer |
| **Python `list`** | Under the hood, it's a dynamic array |

---

## 1.5 Time Complexity Summary

| Operation | Best | Worst | Amortized |
|-----------|------|-------|-----------|
| Access `arr[i]` | O(1) | O(1) | O(1) |
| Append | O(1) | O(n) *(resize)* | O(1) |
| Insert at index | O(n) | O(n) | O(n) |
| Delete at index | O(n) | O(n) | O(n) |
| Pop (last) | O(1) | O(1) | O(1) |
| Find by value | O(n) | O(n) | O(n) |

---

## 1.6 Operations with Visualizations & Code

### Operation 1: Append (Amortized O(1))

**Logic:** If `n == size`, double capacity first. Place new item at index `n`, then increment `n`.

```
Before append(60):          After append(60):
[10, 20, 30, 40, 50]       [10, 20, 30, 40, 50, 60]
 n=5, size=8                 n=6, size=8
```

```python
def append(self, item):
    if self.size == self.n:
        self.__resize(self.size * 2)   # Double capacity when full

    self.A[self.n] = item
    self.n += 1
```

---

### Operation 2: Geometric Resize (O(n))

**Logic:** Allocate a new array 2× larger, copy all existing elements, reassign pointer.

```
Old array (size=4):          New array (size=8):
[10, 20, 30, 40]    ──copy──>  [10, 20, 30, 40, _, _, _, _]
     self.A                         self.A (new)
```

```python
def __resize(self, new_capacity):
    B = self.__make_array(new_capacity)
    self.size = new_capacity
    for i in range(self.n):
        B[i] = self.A[i]
    self.A = B
```

**Why double?** Doubling gives **amortized O(1)** append — the O(n) cost happens rarely, spread over many cheap appends.

---

### Operation 3: Insert at Index (O(n))

**Logic:** Shift elements from `pos` to the right by one slot, then place item at `pos`.

```
Insert 99 at index 2:

Step 1 — shift right:        Step 2 — place 99:
[10, 20, 30, 40, 50]         [10, 20, 99, 30, 40, 50]
       ↑ shift →                    ↑ inserted
```

```python
def insert(self, pos, item):
    if self.n == self.size:
        self.__resize(self.size * 2)

    for i in range(self.n, pos, -1):   # Shift right
        self.A[i] = self.A[i - 1]

    self.A[pos] = item
    self.n += 1
```

---

### Operation 4: Delete at Index (O(n))

**Logic:** Shift all elements after `pos` one slot to the left.

```
Delete index 2 (value 30):

Before:  [10, 20, 30, 40, 50]
After:   [10, 20, 40, 50]
              ↑ shift left
```

```python
def __delitem__(self, pos):
    for i in range(pos, self.n - 1):
        self.A[i] = self.A[i + 1]
    self.n -= 1
```

---

### Operation 5: Pop (O(1))

**Logic:** Decrement `n` and return the last element.

```
Before pop:  [10, 20, 30, 40, 50]  n=5
After pop:   [10, 20, 30, 40]      n=4  → returns 50
```

```python
def pop(self):
    if self.n == 0:
        raise IndexError("pop from empty array")
    self.n -= 1
    return self.A[self.n]
```

---

### Operation 6: Index Access (O(1))

**Logic:** Direct memory lookup. Supports negative indexing (`arr[-1]` = last element).

```python
def __getitem__(self, key):
    if key < 0:
        key = self.n + key
    if 0 <= key < self.n:
        return self.A[key]
    raise IndexError("Index out of bounds")
```

---

### Operation 7: Find & Remove by Value (O(n))

```python
def find(self, item):
    for i in range(self.n):
        if self.A[i] == item:
            return i
    return -1

def remove(self, item):
    pos = self.find(item)
    if pos != -1:
        self.__delitem__(pos)
    else:
        raise ValueError("list.remove(x): x not in list")
```

---

## 1.7 Resize Amortized Analysis (Visual)

```
Appends:  1   2   3   4   5   6   7   8   9  10  11  12 ...
Capacity: 1 → 2 → 4 → 4 → 8 → 8 → 8 → 8 → 16 ...
Resizes:      ↑       ↑               ↑
              copy    copy            copy (costly, but rare)
```

Over `n` appends, total copy work ≈ `n + n/2 + n/4 + ...` < `2n` → **amortized O(1)** per append.

---

# 2. Linked Lists (Singly Linked List)

## 2.1 Introduction

A **singly linked list** is a chain of **nodes** scattered in memory. Each node holds a `value` and a `next` pointer to the following node. The list tracks only the `head` (first node).

```
head
 ↓
┌───────┐    ┌───────┐    ┌───────┐    ┌───────┐
│  10   │───>│  20   │───>│  30   │───>│  40   │───> None
│ next  │    │ next  │    │ next  │    │ next  │
└───────┘    └───────┘    └───────┘    └───────┘
  Node 0       Node 1       Node 2       Node 3
```

Unlike arrays, nodes are **not contiguous** — index 3 can't be reached directly; traversal starts from the head.

---

## 2.2 Real-Life Analogy

A **treasure hunt**:

- Each clue (node) points to where the next clue is (`next` pointer).
- Clue #5 can't be reached without following clues 1→2→3→4.
- Adding a new first clue is instant — just hand someone the new starting clue (O(1) head insert).

---

## 2.3 Merits & Demerits

| ✅ Merits | ❌ Demerits |
|-----------|-------------|
| **O(1) insert/delete at head** | **O(n) access by index** — must traverse |
| **Dynamic size** — no resize needed | **Extra memory** per node (pointer overhead) |
| **No shifting** on insert/delete at known position | **Not cache-friendly** — nodes scattered in RAM |
| Easy to **reverse** and manipulate pointers | **No random access** |

---

## 2.4 Real-Life Examples

| Use Case | Why Linked Lists? |
|----------|-------------------|
| **Browser history (back button)** | Each page points to the previous one |
| **Music playlist "next"** | Each song node links to the next track |
| **Undo chains** | Each state points to the prior state |
| **Hash map collision chains** | Separate chaining uses linked lists |

---

## 2.5 Time Complexity Summary

| Operation | Time | Notes |
|-----------|------|-------|
| Insert Head | O(1) | Pointer reassignment only |
| Insert Tail | O(n) | Must traverse to last node |
| Insert After Value | O(n) | Search + pointer update |
| Delete Head | O(1) | Move head forward |
| Delete Tail | O(n) | Need second-to-last node |
| Delete by Value | O(n) | Search required |
| Search / Access by Index | O(n) | Sequential walk |
| Reverse In-Place | O(n) | Three-pointer technique |
| Length `len()` | O(1) | Tracked via `self.n` |

---

## 2.6 Operations with Visualizations & Code

### Operation 1: Insert at Head (O(1))

```
Before insert_head(5):          After insert_head(5):

head                            head
 ↓                               ↓
[20] -> [30] -> None            [5] -> [20] -> [30] -> None
                                 ↑ new node points to old head
```

```python
def insert_head(self, value):
    new_node = Node(value)
    new_node.next = self.head   # New node points to current head
    self.head = new_node        # Head becomes new node
    self.n += 1
```

---

### Operation 2: Insert at Tail (O(n))

```
Traverse to last node, then attach:

[10] -> [20] -> [30] -> None
                  ↑
               temp (last)
                  |
                  v
[10] -> [20] -> [30] -> [40] -> None
```

```python
def insert_tail(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.n += 1
        return

    temp = self.head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    self.n += 1
```

---

### Operation 3: Insert After Target Value (O(n))

```
Insert 25 after 20:

[10] -> [20] -> [30] -> None
              ↓
         [10] -> [20] -> [25] -> [30] -> None
                    ↑ new node between 20 and 30
```

```python
def insert_after(self, target_value, new_value):
    temp = self.head
    while temp is not None:
        if temp.value == target_value:
            new_node = Node(new_value)
            new_node.next = temp.next
            temp.next = new_node
            self.n += 1
            return
        temp = temp.next
    raise ValueError(f"Target value {target_value} not found.")
```

---

### Operation 4: Delete Head (O(1))

```
Before:  head -> [10] -> [20] -> [30]
After:   head -> [20] -> [30]
         (old head node is garbage-collected)
```

```python
def delete_head(self):
    if self.head is None:
        raise IndexError("Cannot delete from an empty linked list.")
    self.head = self.head.next
    self.n -= 1
```

---

### Operation 5: Delete Tail (O(n))

```
Need to find second-to-last node:

[10] -> [20] -> [30] -> None
         ↑
      temp (second-to-last)
         |
         v
[10] -> [20] -> None
```

```python
def delete_tail(self):
    if self.head.next is None:
        self.delete_head()
        return
    temp = self.head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    self.n -= 1
```

---

### Operation 6: Delete by Value (O(n))

```
Delete 20:

[10] -> [20] -> [30] -> None
  ↑       ↑
 temp  temp.next (target)
         |
         v
[10] ---------> [30] -> None
 (bypass node with value 20)
```

```python
def delete_value(self, value):
    if self.head.value == value:
        self.delete_head()
        return
    temp = self.head
    while temp.next is not None:
        if temp.next.value == value:
            temp.next = temp.next.next   # Skip the target node
            self.n -= 1
            return
        temp = temp.next
    raise ValueError(f"Value {value} not found in list.")
```

---

### Operation 7: Reverse In-Place (O(n)) — Three Pointers

**The classic interview algorithm.** Use `prev`, `curr`, and `next` to flip each arrow.

```
Step-by-step reverse of [10] -> [20] -> [30]:

Initial:  None <- prev   curr -> [10] -> [20] -> [30]

Step 1:   None <- [10]   curr -> [20] -> [30]
Step 2:   None <- [10] <- [20]   curr -> [30]
Step 3:   None <- [10] <- [20] <- [30]   curr=None

Final head = prev (node 30)
```

```python
def reverse_inplace(self):
    prev_node = None
    curr_node = self.head

    while curr_node is not None:
        next_node = curr_node.next   # Save next
        curr_node.next = prev_node   # Flip arrow
        prev_node = curr_node        # Advance prev
        curr_node = next_node        # Advance curr

    self.head = prev_node
```

---

### Operation 8: Search by Value (O(n))

```python
def search_value(self, value):
    temp = self.head
    pos = 0
    while temp is not None:
        if temp.value == value:
            return pos
        temp = temp.next
        pos += 1
    return -1
```

---

### Operation 9: Access by Index (O(n))

```python
def __getitem__(self, idx):
    if idx < 0:
        idx = self.n + idx
    temp = self.head
    for _ in range(idx):
        temp = temp.next
    return temp.value
```

---

## 2.7 Array vs Linked List — Memory Diagram

```
ARRAY (contiguous):                LINKED LIST (scattered):

┌───┬───┬───┬───┐                 RAM Address 0x100: [10|→0x250]
│ 0 │ 1 │ 2 │ 3 │                 RAM Address 0x250: [20|→0x400]
└───┴───┴───┴───┘                 RAM Address 0x400: [30|→0x550]
  fast index access                 RAM Address 0x550: [40|→None]
  slow middle insert                slow index access
                                    fast head insert
```

---

# 3. Queues (FIFO)

## 3.1 Introduction

A **queue** follows **FIFO** — **First In, First Out**. The first element added is the first one removed. Think of a line at a coffee shop.

The linked-list version (`Queues/queues_using_linked_lists.py`) uses two pointers:

- **`front`** — where dequeue happens (remove)
- **`rear`** — where enqueue happens (add)

```
  DEQUEUE here                    ENQUEUE here
       ↓                               ↓
front                              rear
  ↓                                  ↓
[Alice] -> [Bob] -> [Charlie] -> None
  ↑ oldest                           ↑ newest
```

---

## 3.2 Real-Life Analogy

A **supermarket checkout line**:

- New customers join at the **back** (enqueue).
- The cashier serves whoever is at the **front** first (dequeue).
- Nobody cuts in line (FIFO discipline).

---

## 3.3 Merits & Demerits

| ✅ Merits | ❌ Demerits |
|-----------|-------------|
| **Fair ordering** — first come, first served | **No random access** to middle elements |
| **O(1) enqueue & dequeue** (with front/rear pointers) | Linked-list version uses **extra pointer memory** |
| Natural fit for **scheduling & BFS** | Array-based queue can waste space (circular buffer fixes this) |
| Simple, predictable behavior | Cannot easily peek at arbitrary positions |

---

## 3.4 Real-Life Examples

| Use Case | How Queue is Used |
|----------|-------------------|
| **Print spooler** | Documents printed in submission order |
| **BFS graph traversal** | Nodes visited level by level |
| **Task schedulers** | OS processes waiting for CPU time |
| **Customer support tickets** | Oldest ticket handled first |
| **Message brokers (Kafka, RabbitMQ)** | Events consumed in produce order |

---

## 3.5 Time Complexity Summary

| Operation | Time | Notes |
|-----------|------|-------|
| Enqueue | O(1) | Append at `rear` |
| Dequeue | O(1) | Remove at `front` |
| Peek Front | O(1) | Direct `front` access |
| Size / `len()` | O(1) | Via `self.n` |
| Traverse | O(n) | Walk front → rear |
| is_empty | O(1) | Check `front is None` |

---

## 3.6 Operations with Visualizations & Code

### Operation 1: Enqueue (O(1))

```
enqueue("Dave"):

Before:
front                              rear
  ↓                                  ↓
[Alice] -> [Bob] -> [Charlie] -> None

After:
front                                        rear
  ↓                                            ↓
[Alice] -> [Bob] -> [Charlie] -> [Dave] -> None
```

```python
def enqueue(self, item):
    new_node = Node(item)
    if self.rear is None:          # Empty queue — first element
        self.front = new_node
        self.rear = new_node
    else:
        self.rear.next = new_node  # Link old rear to new node
        self.rear = new_node       # Advance rear pointer
    self.n += 1
```

---

### Operation 2: Dequeue (O(1))

```
dequeue() → returns "Alice":

Before:
front                              rear
  ↓                                  ↓
[Alice] -> [Bob] -> [Charlie] -> None

After:
front                    rear
  ↓                        ↓
[Bob] -> [Charlie] -> None
```

```python
def dequeue(self):
    if self.front is None:
        raise IndexError("dequeue from empty queue")

    item = self.front.data
    self.front = self.front.next
    if self.front is None:         # Queue is now empty
        self.rear = None           # Reset both pointers!
    self.n -= 1
    return item
```

> **Critical detail:** When the last element is dequeued, set **both** `front` and `rear` to `None`. Forgetting this breaks future enqueues.

---

### Operation 3: is_empty (O(1))

```python
def is_empty(self):
    return self.front is None
```

---

### Operation 4: Traverse (O(n))

```
Print order (front → rear):  Alice  Bob  Charlie
```

```python
def traverse(self):
    curr = self.front
    while curr is not None:
        print(curr.data, end=' ')
        curr = curr.next
```

---

## 3.7 Queue vs Stack — Side by Side

```
QUEUE (FIFO) — line at a store:     STACK (LIFO) — plate dispenser:

  IN ──> [A][B][C] ──> OUT            IN ──> [C]  ← TOP (OUT)
         front    rear                     [B]
                                           [A]
         First in = first out              Last in = first out
```

---

## 3.8 BFS Uses a Queue (Conceptual)

```
Graph BFS starting at node A:

Queue: [A]
Visit A → enqueue neighbors B, C:  [B, C]
Dequeue B → visit B → enqueue D:    [C, D]
Dequeue C → visit C:                [D]
...

BFS always explores the closest level first — queues guarantee FIFO order.
```

---

# 4. Stacks (LIFO)

## 4.1 Introduction

A **stack** follows **LIFO** — **Last In, First Out**. The most recently added item is removed first. There are **two implementations**:

| Variant | File | Backing Store |
|---------|------|---------------|
| Array Stack | `Stacks/stacks_using_arrays.py` | Fixed-size Python list |
| Linked List Stack | `Stacks/stacks_using_linked_lists.py` | Singly linked list |

---

## 4.2 Real-Life Analogy

A **stack of plates** in a cafeteria:

- New plates go on top (push).
- Plates are always taken from the top (pop).
- The bottom plate has been there the longest and is accessed last.

---

## 4.3 Merits & Demerits

| ✅ Merits | ❌ Demerits |
|-----------|-------------|
| **O(1) push, pop, peek** | **No random access** to middle elements |
| Perfect for **nested/recursive** problems | Array stack has **fixed capacity** (overflow risk) |
| Simple state tracking (undo/redo) | Cannot efficiently remove from bottom |
| Natural for **DFS** and backtracking | Linked-list stack has pointer overhead |

---

## 4.4 Real-Life Examples

| Use Case | How Stack is Used |
|----------|-------------------|
| **Undo/Redo in editors** | Each action pushed; undo = pop |
| **Browser back button** | History stack of visited pages |
| **Function call stack** | Each function call pushes a frame; return = pop |
| **Balanced parentheses check** | Push `(`; pop on `)` |
| **DFS graph traversal** | Explore deepest path first |
| **String reversal** | Push all chars, pop to reverse order |

---

## 4.5 Time Complexity Summary

| Operation | Array Stack | Linked List Stack |
|-----------|-------------|-------------------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| is_empty | O(1) | O(1) |
| Traverse | O(n) | O(n) |

---

## 4.6 Array Stack — Visual Model

```
top = 2 (3 elements stored)

Index:   [0]   [1]   [2]   [3]   [4]
       ┌─────┬─────┬─────┬─────┬─────┐
       │  10 │  20 │  30 │ None│ None│
       └─────┴─────┴─────┴─────┴─────┘
                         ↑
                        top  ← push/pop here

Capacity = 5, Elements = 3
```

### Push (O(1))

```
push(40):

Before (top=2):  [10, 20, 30, _, _]
After  (top=3):  [10, 20, 30, 40, _]
```

```python
def push(self, item):
    if self.top == self.size - 1:
        raise OverflowError("Stack overflow")
    self.top += 1
    self.stack[self.top] = item
```

### Pop (O(1))

```
pop() → returns 40:

Before (top=3):  [10, 20, 30, 40, _]
After  (top=2):  [10, 20, 30, None, _]
```

```python
def pop(self):
    if self.top == -1:
        raise IndexError("pop from empty stack")
    item = self.stack[self.top]
    self.stack[self.top] = None
    self.top -= 1
    return item
```

### Peek (O(1))

```python
def peek(self):
    if self.top == -1:
        raise IndexError("peek from empty stack")
    return self.stack[self.top]
```

---

## 4.7 Linked List Stack — Visual Model

```
top
 ↓
[30] -> [20] -> [10] -> None
 ↑ newest          ↑ oldest (bottom)
```

### Push (O(1)) — Same as Linked List Insert Head

```
push(40):

Before:  [30] -> [20] -> [10] -> None
After:   [40] -> [30] -> [20] -> [10] -> None
```

```python
def push(self, item):
    new_node = Node(item)
    new_node.next = self.top
    self.top = new_node
    self.n += 1
```

### Pop (O(1))

```python
def pop(self):
    if self.is_empty():
        raise IndexError("pop from empty stack")
    data = self.top.data
    self.top = self.top.next
    self.n -= 1
    return data
```

---

## 4.8 Application: String Reversal

**Logic:** Push every character, then pop — LIFO naturally reverses order.

```
Input: "HELLO"

Push:  H → E → L → L → O
Stack (top first):  O, L, L, E, H

Pop:   O + L + L + E + H = "OLLEH"
```

```python
def string_reversal(self, text):
    for ch in text:
        self.push(ch)

    rev = ''
    while not self.is_empty():
        rev += self.pop()
    return rev
```

**Visualization:**

```
"HELLO"
  │ push each char
  ▼
┌───┬───┬───┬───┬───┐
│ O │ L │ L │ E │ H │  ← top
└───┴───┴───┴───┴───┘
  │ pop each char
  ▼
"OLLEH"
```

---

## 4.9 Application: Undo / Redo with Two Stacks

**Logic:**

- **Main stack** = current document state
- **Redo stack** = undone characters waiting to be restored
- `u` (undo) → pop from main, push to redo
- `r` (redo) → pop from redo, push to main

```
Initial text: "ABC"
Main stack (top first): C, B, A

Command "u" (undo):
  Pop C from main → push C to redo
  Main: B, A     Redo: C

Command "r" (redo):
  Pop C from redo → push C to main
  Main: C, B, A  Redo: (empty)
```

```python
def undo_redo(self, text, commands):
    new_stack = Stack()   # Redo stack

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
```

---

## 4.10 Stack vs Queue — Decision Guide

```
                    Need most-recent-first?
                           │
              ┌────────────┴────────────┐
             YES                        NO
              │                          │
           STACK                      QUEUE
    (undo, DFS, recursion)    (scheduling, BFS, tickets)
```

---

# 5. Hash Maps

## 5.1 Introduction

A **hash map** (or dictionary) stores **key-value pairs** and supports fast lookup by key. Instead of scanning every entry, a **hash function** converts a key into an array index — like a shortcut to the right slot.

```
Key "python"  ──hash──>  index 3  ──>  value 105
Key "java"    ──hash──>  index 1  ──>  value 90
```

Two collision-resolution strategies are implemented:

| Variant | File | Strategy |
|---------|------|----------|
| Linear Probing | `Hash_Maps/hashing_using_linear_probing.py` | Open addressing — probe next slot on collision |
| Separate Chaining | `Hash_Maps/hashing_using_chaining.py` | Each bucket holds a linked list of entries |

### The Hash Function (both variants)

```python
def hash_function(self, key):
    return abs(hash(key)) % self.size   # or self.capacity for chaining
```

`hash(key)` produces a large integer; `% size` maps it into a valid table index.

---

## 5.2 Real-Life Analogy

A **coat check at a theater**:

- Each guest gets a **ticket number** (hash index) based on their name.
- The attendant stores the coat in the matching locker (slot/bucket).
- **Collision:** two names map to the same locker → either use the next free locker (linear probing) or hang multiple coats in one locker on hooks (chaining).

---

## 5.3 Merits & Demerits

| ✅ Merits | ❌ Demerits |
|-----------|-------------|
| **O(1) average** lookup, insert, update by key | **Collisions** degrade performance toward O(n) |
| No need to know index in advance | **No sorted order** — keys aren't stored in sequence |
| Ideal for **caches, indexes, frequency counts** | Fixed table size can **fill up** (linear probing) or chains can grow long (chaining) |
| Python `dict` uses a hash table under the hood | Hash function quality matters — bad distribution = more collisions |

---

## 5.4 Real-Life Examples

| Use Case | How Hash Maps Help |
|----------|-------------------|
| **Phone contacts** | Name → phone number in one step |
| **Caching (Redis, memcached)** | URL → cached page content |
| **Word frequency counters** | Word → count |
| **Database indexes** | Primary key → row location |
| **Symbol tables in compilers** | Variable name → memory address |

---

## 5.5 Time Complexity Summary

| Operation | Average | Worst Case | Notes |
|-----------|---------|------------|-------|
| Put / Update | O(1) | O(n) | Worst when table is crowded or chains are long |
| Get | O(1) | O(n) | Must probe or walk chain on collision |
| Contains (`key in d`) | O(1) | O(n) | Linear probing: uses `get` internally |
| Clear | O(n) | O(n) | Reset all slots/buckets |
| Rehash | O(n) | O(n) | Re-insert all entries into larger table |

---

## 5.6 Collisions — What Happens?

A **collision** occurs when two different keys hash to the same index.

```
Keys "cat" and "act" might both hash to index 2:

Linear Probing:              Separate Chaining:
Index 2: [cat]               Bucket 2: cat→5 ──> act→8 ──> None
Index 3: [act]  (next slot)
```

---

# 5A. Linear Probing (Open Addressing)

## 5A.1 How It Works

The table has two parallel arrays:

- **`slots`** — stores keys (or `None` if empty)
- **`data`** — stores values at the same index

On collision, probe the **next** index: `(index + 1) % size`, wrapping around the table.

```
Table size = 7

put("apple", 10)  → hash → slot 3  →  [apple:10]
put("grape", 20)  → hash → slot 3  →  occupied!
                      probe → slot 4  →  [grape:20]

Slots:  [_, _, _, apple, grape, _, _]
Data:   [_, _, _,   10,    20, _, _]
Index:   0  1  2    3      4   5  6
```

---

## 5A.2 Operations with Visualizations & Code

### Operation 1: Put (O(1) average)

**Logic:**

1. Hash the key to get `hash_value`.
2. If slot is empty → store key and value.
3. If slot has the **same key** → update value.
4. Otherwise → probe forward until an empty slot or matching key is found.

```
put("dog", 30) when slots 3 and 4 are taken, hash lands on 3:

Start at 3 → occupied (apple)
Probe  4 → occupied (grape)
Probe  5 → empty   → store dog:30
```

```python
def put(self, key, value):
    hash_value = self.hash_function(key)

    if self.slots[hash_value] is None:
        self.slots[hash_value] = key
        self.data[hash_value] = value
        self.n += 1
        return

    if self.slots[hash_value] == key:
        self.data[hash_value] = value
        return

    new_hash_value = self.rehash(hash_value)
    while self.slots[new_hash_value] is not None and self.slots[new_hash_value] != key:
        new_hash_value = self.rehash(new_hash_value)
        if new_hash_value == hash_value:
            raise OverflowError("hash table is full")

    if self.slots[new_hash_value] is None:
        self.slots[new_hash_value] = key
        self.data[new_hash_value] = value
        self.n += 1
    else:
        self.data[new_hash_value] = value
```

### Operation 2: Probe Step (O(1) per step)

```python
def rehash(self, old_hash_value):
    return (old_hash_value + 1) % self.size
```

### Operation 3: Get (O(1) average)

**Logic:** Start at the hashed index, probe forward until the key is found or an empty slot is hit (key doesn't exist).

```
get("grape") → hash → 3
  slot 3 = apple  → keep probing
  slot 4 = grape  → return data[4] = 20
```

```python
def get(self, key):
    start_position = self.hash_function(key)

    if self.slots[start_position] is None:
        raise KeyError(key)

    current_position = start_position
    while True:
        if self.slots[current_position] == key:
            return self.data[current_position]

        current_position = self.rehash(current_position)

        if current_position == start_position:
            raise KeyError(key)

        if self.slots[current_position] is None:
            raise KeyError(key)
```

### Operation 4: Bracket Access & Membership

```python
def __getitem__(self, key):
    return self.get(key)

def __setitem__(self, key, value):
    self.put(key, value)

def __contains__(self, key):
    try:
        self.get(key)
        return True
    except KeyError:
        return False
```

### Operation 5: Clear (O(n))

```python
def clear(self):
    self.slots = [None] * self.size
    self.data = [None] * self.size
    self.n = 0
```

---

## 5A.3 Linear Probing — Pros & Cons

| ✅ Pros | ❌ Cons |
|---------|---------|
| Simple — one array, cache-friendly | **Clustering** — filled runs of slots slow probing |
| No extra pointer memory per entry | Table can fill up → `OverflowError` |
| Good when load factor stays low | Deletes are tricky (need tombstone markers) |

---

# 5B. Separate Chaining

## 5B.1 How It Works

The table is an **array of buckets**. Each bucket is a **linked list** of `Node(key, value)` pairs. Multiple keys that hash to the same index share one bucket chain.

```
capacity = 5

buckets[0]: Empty Bucket
buckets[1]: python --> 105
buckets[2]: java --> 90 --> rust --> 80
buckets[3]: Empty Bucket
buckets[4]: go --> 70
```

```
         hash("java")  = 2
         hash("rust")  = 2   (collision!)
              │
              ▼
buckets[2]:  [java|90] ──> [rust|80] ──> None
```

---

## 5B.2 Operations with Visualizations & Code

### Operation 1: Put (O(1) average)

**Logic:**

1. Hash key → `bucket_index`.
2. Search the bucket's linked list for the key.
3. Key not found → append new node at tail.
4. Key found → update the node's value.
5. If load factor gets too high → **rehash** (double capacity, re-insert all entries).

```
put("rust", 80) when bucket 2 already has java:

Before:  java --> 90
After:   java --> 90 --> rust --> 80
```

```python
def put(self, key, value):
    bucket_index = self.hash_function(key)
    node_index = self.get_node_index(bucket_index, key)

    if node_index == -1:
        self.buckets[bucket_index].insert_tail(key, value)
        self.n += 1
        if (self.n / self.capacity >= 2):
            self.rehash()
    else:
        node = self.buckets[bucket_index].get_node_at_index(node_index)
        node.value = value
```

### Operation 2: Get (O(1) average)

```python
def get(self, key):
    bucket_index = self.hash_function(key)
    res = self.buckets[bucket_index].search_value(key)

    if res == -1:
        return -1
    else:
        node = self.buckets[bucket_index].get_node_at_index(res)
        return node.value
```

### Operation 3: Search Within a Bucket (O(k))

`k` = number of nodes in that bucket's chain.

```python
def search_value(self, key):
    temp = self.head
    pos = 0
    while temp is not None:
        if temp.key == key:
            return pos
        temp = temp.next
        pos += 1
    return -1
```

### Operation 4: Rehash (O(n))

**Logic:** Double the bucket count, create fresh empty buckets, re-insert every key-value pair.

```
Old capacity = 4, n = 6  →  load factor too high

New capacity = 8
Re-insert all 6 pairs into fresh buckets using new hash indices
```

```python
def rehash(self):
    self.capacity = self.capacity * 2
    old_buckets = self.buckets
    self.n = 0
    self.buckets = self.make_array(self.capacity)

    for bucket in old_buckets:
        for j in range(bucket.n):
            node = bucket.get_node_at_index(j)
            self.put(node.key, node.value)
```

---

## 5B.3 Separate Chaining — Pros & Cons

| ✅ Pros | ❌ Cons |
|---------|---------|
| No table overflow — chains can grow | Extra memory per node (key, value, pointer) |
| Deletion is straightforward (unlink node) | Long chains degrade to O(n) lookup |
| Load factor can exceed 1.0 | Not as cache-friendly as contiguous slots |
| Reuses linked list skills from earlier modules | Rehashing re-inserts every entry |

---

## 5.7 Linear Probing vs Separate Chaining

```
LINEAR PROBING                    SEPARATE CHAINING
─────────────────                 ─────────────────
One array of slots                Array of linked lists
Collision → next slot             Collision → same bucket chain
Risk: clustering                  Risk: long chains
Memory: compact                   Memory: pointers per entry
Delete: needs tombstones          Delete: unlink from chain
```

| Factor | Linear Probing | Separate Chaining |
|--------|----------------|-------------------|
| Collision handling | Probe forward | Append to linked list |
| Max load factor | Must stay < 1 | Can exceed 1 |
| Memory overhead | Low | Higher (node pointers) |
| Implementation complexity | Moderate | Builds on linked lists |
| Worst-case lookup | O(n) clustered slots | O(n) long chain |

---

# 6. Quick Comparison Cheat Sheet

## 6.1 All Structures at a Glance

| Structure | Order | Access Pattern | Best At |
|-----------|-------|----------------|---------|
| **Array** | Indexed | Random O(1) | Fast lookups, iteration |
| **Linked List** | Sequential | Head O(1), index O(n) | Frequent head insert/delete |
| **Queue** | FIFO | Front/rear O(1) | Fair scheduling, BFS |
| **Stack** | LIFO | Top O(1) | Undo, DFS, nesting |
| **Hash Map** | Unordered | Key lookup O(1) avg | Fast key-value access |

---

## 6.2 When to Pick Which?

```
┌─────────────────────────────────────────────────────────────┐
│  "I need fast access by index"           →  ARRAY          │
│  "I insert/delete at the beginning a lot"  →  LINKED LIST    │
│  "First come, first served"                →  QUEUE          │
│  "Last action matters most"                →  STACK          │
│  "I need fast lookup by key"               →  HASH MAP      │
└─────────────────────────────────────────────────────────────┘
```

---

## 6.3 Complexity Comparison Table

| Operation | Array | Linked List | Queue (LL) | Stack (LL) | Hash Map |
|-----------|-------|-------------|------------|------------|----------|
| Access by index | O(1) | O(n) | — | — | — |
| Lookup by key | O(n) | O(n) | O(n) | O(n) | O(1)* |
| Insert at beginning | O(n) | O(1) | — | O(1) push | — |
| Insert at end | O(1)† | O(n) | O(1) enqueue | — | O(1)* put |
| Delete beginning | O(n) | O(1) | O(1) dequeue | O(1) pop | — |
| Search by value | O(n) | O(n) | O(n) | O(n) | — |

*† Amortized O(1) for dynamic array append*
*\* Average case; O(n) worst case when collisions cluster*

---

## 6.4 Relationship Diagram

```
                    LINEAR DATA STRUCTURES
                              │
        ┌─────────┬───────────┼───────────┬─────────┐
        │         │           │           │         │
     ARRAY    LINKED LIST   QUEUE       STACK    HASH MAP
   (contiguous) (nodes)    (FIFO)      (LIFO)   (key→value)
        │         │           │           │         │
        │         └─────┬─────┘           │    uses linked
        │               │                 │    lists for
        │         Both built on        Both O(1)  chaining
        │         linked lists         top/front │
        │               │                 │         │
        └───────────────┴─────────────────┴─────────┘
                  Foundation for
              trees, graphs, hash tables
```

---

## 6.5 How to Run the Modules

```bash
python3 Arrays/dynamic_array.py
python3 Linked_Lists/linked_lists.py
python3 Queues/queues_using_linked_lists.py
python3 Stacks/stacks_using_arrays.py
python3 Stacks/stacks_using_linked_lists.py
python3 Hash_Maps/hashing_using_linear_probing.py
```

Linear probing has an interactive CLI. The chaining variant can be imported and used directly from `Hash_Maps/hashing_using_chaining.py`.
