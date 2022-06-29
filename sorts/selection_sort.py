import time


def selection_sort(array, drawData, timeTick):
    for step in range(len(array)):
        min_idx = step
        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i
            drawData(array, ['yellow' if x == min_idx or x == i else 'green' for x in range(len(array))])
            time.sleep(timeTick)
        (array[step], array[min_idx]) = (array[min_idx], array[step])
