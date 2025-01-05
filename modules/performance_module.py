# modules/performance_module.py
import time
import tracemalloc
from .data_operations_module import DataOperations

class Performance:
    def run_benchmark(self, operation, algorithm):
        if operation == "sort":
            data = list(range(10000, 0, -1))
            tracemalloc.start()
            start_time = time.time()
            if algorithm == "merge":
                DataOperations().merge_sort(data)
            elif algorithm == "quick":
                DataOperations().quick_sort(data)
            elif algorithm == "heap":
                DataOperations().heap_sort(data)
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"Time Taken: {end_time - start_time} seconds")
            print(f"Memory Usage: Current={current / 1024} KB; Peak={peak / 1024} KB")
