import time


def shaker_sort(array, drawData, timeTick):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped is True:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                drawData(array, ['yellow' if x == i or x == i + 1 else 'green' for x in range(len(array))])
                time.sleep(timeTick)
        if swapped is False:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                drawData(array, ['yellow' if x == i or x == i + 1 else 'green' for x in range(len(array))])
                time.sleep(timeTick)
        start = start + 1
