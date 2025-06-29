class DirectedGraph:
    def __init__(self):
        self.vertices = {}
        self.outgoing = {}
        self.incoming = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = True
            self.outgoing[vertex] = []
            self.incoming[vertex] = []

    def add_edge(self, from_v, to_v):
        if from_v in self.vertices and to_v in self.vertices:
            if to_v not in self.outgoing[from_v]:
                self.outgoing[from_v].append(to_v)
            if from_v not in self.incoming[to_v]:
                self.incoming[to_v].append(from_v)

    def list_outgoing_adjacent_vertex(self, vertex):
        return self.outgoing.get(vertex, [])

    def list_incoming_adjacent_vertex(self, vertex):
        return self.incoming.get(vertex, [])


class Person:
    def __init__(self, name, gender, bio):
        self.name = name
        self.gender = gender
        self.bio = bio

    def __str__(self):
        return f"Name: {self.name}\nGender: {self.gender}\nBio: {self.bio}"


def main():
    # Create social network with sample data (5 people)
    people = [
        Person("Alice", "Female", "Admin"),
        Person("Bob", "Male", "Cybersecurity"),
        Person("Charlie", "Male", "Lecturer"),
        Person("Diana", "Female", "Dancer"),
        Person("Eve", "Female", "Artist")
    ]

    graph = DirectedGraph()
    for person in people:
        graph.add_vertex(person)

    # Create follow relationships
    graph.add_edge(people[0], people[1])  # Alice, Bob
    graph.add_edge(people[0], people[2])  # Alice, Charlie
    graph.add_edge(people[1], people[0])  # Bob, Alice
    graph.add_edge(people[1], people[3])  # Bob, Diana
    graph.add_edge(people[2], people[3])  # Charlie, Diana
    graph.add_edge(people[3], people[4])  # Diana, Eve
    graph.add_edge(people[4], people[0])  # Eve, Alice

    # Menu system with only mandatory features
    while True:
        print("\n" + "*" * 50)
        print("Welcome to Slow Gram, Your New Social Media App:")
        print("*" * 50)
        print("1. View names of all profiles")
        print("2. View details of any profiles")
        print("3. View followed account of any profile")
        print("4. View followers of any profile")
        print("5. Exit")
        print("*" * 50)
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("=" * 50)
            print("VIEW ALL PROFILE NAMES:")
            print("=" * 50)
            for i, person in enumerate(people):
                print(f"{i + 1}. {person.name}")

        elif choice == "2":
            print("=" * 50)
            print("VIEW DETAILS FOR ANY PROFILE:")
            print("=" * 50)
            for i, person in enumerate(people):
                print(f"{i + 1}. {person.name}")

            try:
                idx = int(input("\nSelect a user number: ")) - 1
                if 0 <= idx < len(people):
                    print("\n" + "=" * 50)
                    print(f"PROFILE DETAILS: {people[idx].name}")
                    print("=" * 50)
                    print(people[idx])
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Invalid input!")

        elif choice == "3":
            print("=" * 50)
            print("VIEW FOLLOWED ACCOUNTS")
            print("=" * 50)
            for i, person in enumerate(people):
                print(f"{i + 1}. {person.name}")

            try:
                idx = int(input("\nSelect a user number: ")) - 1
                if 0 <= idx < len(people):
                    followed = graph.list_outgoing_adjacent_vertex(people[idx])
                    print("\n" + "=" * 50)
                    print(f"{people[idx].name}'s FOLLOWED ACCOUNTS")
                    print("=" * 50)
                    if followed:
                        for p in followed:
                            print(f"- {p.name}")
                    else:
                        print("No followed accounts")
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Invalid input!")

        elif choice == "4":
            print("=" * 50)
            print("VIEW FOLLOWERS")
            print("=" * 50)
            for i, person in enumerate(people):
                print(f"{i + 1}. {person.name}")

            try:
                idx = int(input("\nSelect a user number: ")) - 1
                if 0 <= idx < len(people):
                    followers = graph.list_incoming_adjacent_vertex(people[idx])
                    print("\n" + "=" * 50)
                    print(f"{people[idx].name}'s FOLLOWERS")
                    print("=" * 50)
                    if followers:
                        for p in followers:
                            print(f"- {p.name}")
                    else:
                        print("No followers")
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Invalid input!")

        elif choice == "5":
            print("\nExiting program.")
            break

        else:
            print("Invalid choice! Please enter 1-5")


if __name__ == "__main__":
    main()