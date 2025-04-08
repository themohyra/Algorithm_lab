import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 50

result = linear_search(arr, x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)

n = [10, 20, 50, 100, 200, 500, 1000]
time = [0.0001, 0.0003, 0.0008, 0.0015, 0.0030, 0.0075, 0.0150]

plt.plot(n, time)
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken')
plt.title('Time Complexity of Linear Search')
plt.show()

    execution_time = timeit.timeit(test_code, setup=setup_code, number=1)
    time_taken.append(execution_time)

plt.plot(list_lengths, time_taken)
plt.xlabel('Size of array')
plt.ylabel('Time taken (seconds)')
plt.title('Time Complexity of Heap Sort')
plt.show()
