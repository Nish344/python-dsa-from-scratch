class Dictionary:
    """
    A hash map implementation using open addressing with linear probing.
    Stores key-value pairs in parallel slots and data arrays.
    """
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.n = 0

    def __len__(self):
        """Returns the number of key-value pairs stored (O(1))."""
        return self.n

    def hash_function(self, key):
        """Maps a key to an index in the table (O(1))."""
        return abs(hash(key)) % self.size

    def rehash(self, old_hash_value):
        """Returns the next index to probe on collision (O(1))."""
        return (old_hash_value + 1) % self.size

    def put(self, key, value):
        """Inserts or updates a key-value pair (O(1) average, O(n) worst)."""
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

    def get(self, key):
        """Returns the value for a key (O(1) average, O(n) worst)."""
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

    def __getitem__(self, key):
        """Allows bracket access, e.g., d['python'] (O(1) average)."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Allows bracket assignment, e.g., d['python'] = 105 (O(1) average)."""
        self.put(key, value)

    def __contains__(self, key):
        """Supports 'key in d' membership checks (O(1) average)."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def clear(self):
        """Empties the hash table (O(n))."""
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.n = 0

    def keys(self):
        """Returns all stored keys (O(n))."""
        return [key for key in self.slots if key is not None]

    def values(self):
        """Returns all stored values (O(n))."""
        return [self.data[i] for i in range(self.size) if self.slots[i] is not None]

    def items(self):
        """Returns all key-value pairs (O(n))."""
        return [(self.slots[i], self.data[i]) for i in range(self.size) if self.slots[i] is not None]

    def __str__(self):
        """Prints the dictionary in standard Python dict format."""
        if self.n == 0:
            return '{}'

        pairs = [f"{key!r}: {value!r}" for key, value in self.items()]
        return '{' + ', '.join(pairs) + '}'


def main():
    """Interactive CLI for the Hash Map (Linear Probing)."""
    try:
        capacity = int(input("Enter hash table capacity: "))
        if capacity < 1:
            raise ValueError
    except ValueError:
        print("Invalid capacity. Using default of 7.")
        capacity = 7

    d = Dictionary(capacity)
    print("=== Hash Map (Linear Probing) Interactive CLI ===")

    while True:
        print("\n" + "-" * 35)
        print(f"Current Map: {d}")
        print(f"Metrics -> Capacity: {d.size} | Entries: {len(d)}")
        print("-" * 35)
        print("1. Put key-value pair")
        print("2. Get value by key")
        print("3. Check if key exists")
        print("4. Clear map")
        print("5. Show internal slots")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        try:
            if choice == '1':
                key = input("Enter key: ")
                value = input("Enter value: ")
                d.put(key, value)
            elif choice == '2':
                key = input("Enter key to fetch: ")
                print(f">> Value: {d.get(key)}")
            elif choice == '3':
                key = input("Enter key to check: ")
                if key in d:
                    print(f">> Key {key!r} exists.")
                else:
                    print(f">> Key {key!r} not found.")
            elif choice == '4':
                d.clear()
                print(">> Map cleared.")
            elif choice == '5':
                print(f"Slots: {d.slots}")
                print(f"Data:  {d.data}")
            elif choice == '6':
                print("Exiting CLI...")
                break
            else:
                print(">> Invalid choice. Please enter a number between 1 and 6.")
        except Exception as e:
            print(f">> ERROR: {e}")


if __name__ == '__main__':
    main()
