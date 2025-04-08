import timeit
import random
import matplotlib.pyplot as plt

# Heapify function to maintain the heap property
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


def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


list_lengths = [10000, 20000, 30000, 50000, 60000]
time_taken = []


for length in list_lengths:

    arr = [random.randint(1, 100000) for _ in range(length)]


    setup_code = "from __main__ import heapSort"
    test_code = f"heapSort({arr})"


    execution_time = timeit.timeit(test_code, setup=setup_code, number=1)
    time_taken.append(execution_time)

plt.plot(list_lengths, time_taken)
plt.xlabel('Size of array')
plt.ylabel('Time taken (seconds)')
plt.title('Time Complexity of Heap Sort')
plt.show()
