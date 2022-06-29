import time


def insertion_sort(array, drawData, timeTick):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            drawData(array, ['yellow' if x == j or x == j + 1 else 'green' for x in range(len(array))])
            time.sleep(timeTick)
        array[j + 1] = key
