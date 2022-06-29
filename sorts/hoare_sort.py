import time


def partition(array, low, high, drawData, timeTick):
    pivot = array[low]
    (i, j) = (low - 1, high + 1)
    while True:
        while True:
            i = i + 1
            if array[i] >= pivot:
                break
        while True:
            j = j - 1
            if array[j] <= pivot:
                break
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
        drawData(array, ['yellow' if x == i or x == j else 'green' for x in range(len(array))])
        time.sleep(timeTick)


def quick_sort(array, low, high, drawData, timeTick):
    if low >= high:
        return
    pivot = partition(array, low, high, drawData, timeTick)
    quick_sort(array, low, pivot, drawData, timeTick)
    quick_sort(array, pivot + 1, high, drawData, timeTick)
