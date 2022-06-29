import time


def bubble_sort(array, drawData, timeTick):
    size = len(array)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                drawData(array, ['yellow' if x == j or x == j + 1 else 'green' for x in range(len(array))])
                time.sleep(timeTick)

    drawData(array, ['green' for x in range(len(array))])
