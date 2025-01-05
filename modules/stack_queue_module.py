# modules/stack_queue_module.py

class Stack:
    def __init__(self):
        """
        Initialize the Stack class with attributes for two stacks sharing the same array.
        - `size`: The total size of the shared array.
        - `stack1_top`: Tracks the top index of the first stack (starts at -1).
        - `stack2_top`: Tracks the top index of the second stack (starts at `size`).
        - `shared_array`: The shared array where both stacks store their elements.
        """
        self.array = []
        self.size = 10  # Total size of the shared array
        self.stack1_top = -1  # Top of the first stack
        self.stack2_top = self.size  # Top of the second stack
        self.shared_array = [None] * self.size  # Shared array for two stacks

    def push(self, value, stack_number=1):
        """
        Push a value onto one of the two stacks.
        Args:
        - value: The value to be pushed onto the stack.
        - stack_number: Indicates which stack to push the value onto (1 or 2).
        
        Checks for overflow to ensure stacks do not overlap.
        """
        if self.stack1_top + 1 == self.stack2_top:  # Check for overflow
            print("Stack Overflow")
            return
        if stack_number == 1:  # Push to Stack 1
            self.stack1_top += 1
            self.shared_array[self.stack1_top] = value
        elif stack_number == 2:  # Push to Stack 2
            self.stack2_top -= 1
            self.shared_array[self.stack2_top] = value

    def pop(self, stack_number=1):
        """
        Pop a value from one of the two stacks.
        Args:
        - stack_number: Indicates which stack to pop the value from (1 or 2).
        
        Handles underflow conditions for both stacks.
        """
        if stack_number == 1:  # Pop from Stack 1
            if self.stack1_top == -1:  # Check for underflow
                print("Stack Underflow")
            else:
                print("Popped:", self.shared_array[self.stack1_top])
                self.shared_array[self.stack1_top] = None  # Clear the popped value
                self.stack1_top -= 1  # Update the top pointer
        elif stack_number == 2:  # Pop from Stack 2
            if self.stack2_top == self.size:  # Check for underflow
                print("Stack Underflow")
            else:
                print("Popped:", self.shared_array[self.stack2_top])
                self.shared_array[self.stack2_top] = None  # Clear the popped value
                self.stack2_top += 1  # Update the top pointer

    def display(self):
        """
        Display the contents of both stacks.
        - Stack 1 elements are displayed from the start of the array up to `stack1_top`.
        - Stack 2 elements are displayed from `stack2_top` to the end of the array.
        """
        print("Stack 1:", self.shared_array[:self.stack1_top + 1])
        print("Stack 2:", self.shared_array[self.stack2_top:])



class Queue:
    class Node:
        """
        Inner class to represent a node in the queue.
        Each node contains a value and a reference to the next node.
        """
        def __init__(self, value):
            self.value = value  # The value stored in the node
            self.next = None  # Pointer to the next node in the queue

    def __init__(self):
        """
        Initialize an empty queue.
        - `front`: Points to the first node in the queue.
        - `rear`: Points to the last node in the queue.
        - `size`: Tracks the number of elements in the queue.
        """
        self.front = None  # Front of the queue (head)
        self.rear = None  # Rear of the queue (tail)
        self.size = 0  # Number of elements in the queue

    def enqueue(self, value):
        """
        Add a new element to the rear of the queue.
        Args:
        - value: The value to be added to the queue.
        """
        new_node = self.Node(value)  # Create a new node with the given value
        if self.rear:  # If the queue is not empty, link the new node to the current rear
            self.rear.next = new_node
        self.rear = new_node  # Update the rear to the new node
        if not self.front:  # If the queue was empty, update the front to the new node
            self.front = new_node
        self.size += 1  # Increment the size of the queue

    def dequeue(self):
        """
        Remove and return the element from the front of the queue.
        Raises:
        - IndexError: If the queue is empty.
        """
        if self.front is None:  # Check for underflow condition
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue")
        value = self.front.value  # Retrieve the value from the front node
        self.front = self.front.next  # Update the front pointer to the next node
        if self.front is None:  # If the queue becomes empty, reset the rear pointer
            self.rear = None
        self.size -= 1  # Decrement the size of the queue
        return value

    def is_empty(self):
        """
        Check if the queue is empty.
        Returns:
        - True if the queue is empty, False otherwise.
        """
        return self.front is None

    def peek(self):
        """
        Retrieve the value at the front of the queue without removing it.
        Raises:
        - IndexError: If the queue is empty.
        """
        if self.is_empty():  # Check if the queue is empty
            raise IndexError("Queue is empty: Cannot peek")
        return self.front.value  # Return the value at the front of the queue

