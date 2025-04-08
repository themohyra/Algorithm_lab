import matplotlib.pyplot as plt

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]

x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0.0, 0.1, 0.3, 0.5, 0.7, 1.0, 1.3, 1.5, 1.8]

plt.plot(x, y)
plt.xlabel('Size of array')
plt.ylabel('Time Complexity')
plt.title('Time Complexity of Insertion Sort')
plt.show()
