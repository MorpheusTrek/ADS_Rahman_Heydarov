from modules.graph_module import GraphModule
from modules.stack_queue_module import Stack, Queue

def main():
    while True:
        print("\nMulti-Functional Data Analysis Platform")
        print("1. Graph Operations")
        print("2. Sorting Operations")
        print("3. Searching Operations")
        print("4. Stack Operations")
        print("5. Queue Operations")
        print("6. Performance Benchmarking")
        print("7. Exit")
        choice = input("Select an option (1-7): ")

        if choice == "1":
            graph_operations()
        elif choice == "2":
            sorting_operations()
        elif choice == "3":
            searching_operations()
        elif choice == "4":
            stack_operations()
        elif choice == "5":
            queue_operations()
        elif choice == "6":
            performance_benchmarking()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def graph_operations():
    graph = GraphModule()
    print("\nGraph Operations")
    print("1. Add Task with Dependencies")
    print("2. Display Graph")
    print("3. Topological Sort")
    action = input("Select an option (1-3): ")

    if action == "1":
        tasks = input("Enter tasks and dependencies (space-separated): ").split()
        if tasks:
            graph.add_task(tasks)
        else:
            print("Error: No tasks provided.")
    elif action == "2":
        graph.display()
    elif action == "3":
        graph.topological_sort()
    else:
        print("Invalid choice.")

def sorting_operations():
    pass

def searching_operations():
    pass

def stack_operations():
    stack = Stack()
    print("\nStack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    action = input("Select an action (1-3): ")

    if action == "1":
        try:
            value = int(input("Enter value to push: "))
            stack.push(value)
        except ValueError:
            print("Error: Invalid input. Please enter an integer value.")
    elif action == "2":
        stack.pop()
    elif action == "3":
        stack.display()
    else:
        print("Invalid choice.")

def queue_operations():
    queue = Queue()
    print("\nQueue Operations")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    action = input("Select an action (1-3): ")

    if action == "1":
        try:
            value = int(input("Enter value to enqueue: "))
            queue.enqueue(value)
        except ValueError:
            print("Error: Invalid input. Please enter an integer value.")
    elif action == "2":
        queue.dequeue()
    elif action == "3":
        queue.display()
    else:
        print("Invalid choice.")

def performance_benchmarking():
    pass

if __name__ == "__main__":
    main()