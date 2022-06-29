import time


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array, drawData, timeTick):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
        drawData(array, ['yellow' if x == i else 'green' for x in range(len(array))])
        time.sleep(timeTick)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        drawData(array, ['yellow' if x == i else 'green' for x in range(len(array))])
        time.sleep(timeTick)