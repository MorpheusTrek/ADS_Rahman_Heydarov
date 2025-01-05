# Multi-Functional Data Analysis Platform

Welcome to the **Multi-Functional Data Analysis Platform**! This Python application provides various tools for graph analysis, sorting, searching, stack and queue operations, and performance benchmarking. 

---

## Table of Contents

1. [Features](#features)
2. [Usage](#usage)
    - [Graph Operations](#graph-operations)
    - [Sorting Operations](#sorting-operations)
    - [Searching Operations](#searching-operations)
    - [Stack Operations](#stack-operations)
    - [Queue Operations](#queue-operations)
    - [Performance Benchmarking](#performance-benchmarking)

---

## Features

- **Graph Operations**: Add tasks with dependencies, visualize graphs, and perform topological sorts.
- **Sorting**: Choose from merge sort, quick sort, and heap sort to sort dataset files.
- **Searching**: Perform binary or linear search on dataset files.
- **Stack and Queue Operations**: Use basic stack and queue functionality such as push/pop and enqueue/dequeue.
- **Performance Benchmarking**: Run performance tests for sorting algorithms.

---

## Usage

Run the application by executing the following command:
```bash
python main.py
```

You will be presented with a menu to choose the desired operation. Follow the prompts for each feature.

### Graph Operations

1. **Add Task with Dependencies**: Enter tasks and dependencies in space-separated format (e.g., `A B` for task `A` depending on task `B`).
2. **Display Graph**: Visualize the graph.
3. **Topological Sort**: Perform a topological sort of tasks.

### Sorting Operations

1. **Merge Sort**
2. **Quick Sort**
3. **Heap Sort**

For each, provide the file path to a dataset and the application will sort the data using the selected algorithm.

### Searching Operations

1. **Binary Search**
2. **Linear Search**

Provide the file path to a dataset and the value to search for.

### Stack Operations

1. **Push**: Add a value to the stack.
2. **Pop**: Remove the top value from the stack.
3. **Display Stack**: View all items in the stack.

### Queue Operations

1. **Enqueue**: Add a value to the queue.
2. **Dequeue**: Remove the front value from the queue.
3. **Display Queue**: View all items in the queue.

### Performance Benchmarking

Run performance benchmarks for sorting algorithms by specifying the algorithm name (e.g., `merge`, `quick`, `heap`).

---
