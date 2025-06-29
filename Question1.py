import random


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.collisions = 0

    def folding_hash(self, key_str):
        # Separate 12 digits into 4-digit part length
        parts = [key_str[i:i + 4] for i in range(0, 12, 4)]
        # Reverse every alternate part (1-based index: 2nd part)
        for i in range(1, len(parts), 2):
            parts[i] = parts[i][::-1]
        # Sum parts and mod by table size
        return sum(int(part) for part in parts) % self.capacity

    def insert_item(self, ic):
        index = self.folding_hash(ic)
        if self.table[index]:
            self.collisions += 1
        self.table[index].append(ic)

    def display_hash(self):
        print("\nHash Table Contents:")
        for i in range(self.capacity):
            items = self.table[i]
            if items:
                # Format: table[i] --> value1 --> value2 --> ...
                values = " --> ".join(items)
                print(f"table[{i}] --> {values}")
            else:
                print(f"table[{i}]")


def generate_ic():
    # Generate random IC Number
    return ''.join(str(random.randint(0, 9)) for _ in range(12))


def main():
    table_sizes = [1009, 2003]
    results = {size: [] for size in table_sizes}

    for size in table_sizes:
        print(f"\n\n{'=' * 70}")
        print(f"Hash Table with Size: {size}")
        print(f"{'=' * 70}")

        for round_num in range(1, 11):
            # Initialize hash table
            hash_table = HashTable(size)

            # Insert 1000 IC numbers
            for _ in range(1000):
                ic = generate_ic()
                hash_table.insert_item(ic)

            # Record collisions
            results[size].append(hash_table.collisions)
            print(f"Round {round_num}: Total Collisions = {hash_table.collisions}")

            # Display full table for first round
            if round_num == 1:
                hash_table.display_hash()

        # Calculate average collisions
        avg_collisions = sum(results[size]) / 10
        print(f"\nAverage Collisions for Size {size}: {avg_collisions:.2f}")

    # Final summary
    print("\n\nSUMMARY OF RESULTS:")
    print("Table Size | Average Collisions")
    print("-----------|-------------------")
    for size in table_sizes:
        print(f"{size:10} | {sum(results[size]) / 10:.2f}")


if __name__ == "__main__":
    main()