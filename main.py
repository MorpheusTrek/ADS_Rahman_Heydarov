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