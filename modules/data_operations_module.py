# modules/data_operations_module.py
import pandas as pd
import numpy as np

class DataOperations:
    def sort_file(self, file_path, algorithm):
        df = pd.read_csv(file_path)
        data = df[df.columns[0]].tolist() 
        if algorithm == "merge":
            sorted_data = self.merge_sort(data)
        elif algorithm == "quick":
            sorted_data = self.quick_sort(data)
        elif algorithm == "heap":
            sorted_data = self.heap_sort(data)
        print("Sorted Data:", sorted_data)

    def search_file(self, file_path, search_type, value):
        data = pd.read_csv(file_path).squeeze().tolist()
        if search_type == "binary":
            result = self.binary_search(data, value)
        elif search_type == "linear":
            result = self.linear_search(data, value)
        print("Search Result:", result)

    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array

    def quick_sort(self, array):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def heap_sort(self, array):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            heapify(array, n, i)
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, i, 0)
        return array

    def binary_search(self, array, value):
        array.sort()
        low, high = 0, len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            if array[mid] == value:
                return mid
            elif array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def linear_search(self, array, value):
        for index, element in enumerate(array):
            if element == value:
                return index
        return -1