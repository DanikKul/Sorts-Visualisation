import time


def gnome_sort(array, drawData, timeTick):
    index = 0
    while index < len(array):
        if index == 0:
            index = index + 1
        if array[index] >= array[index - 1]:
            index = index + 1
        else:
            array[index], array[index - 1] = array[index - 1], array[index]
            index = index - 1
        drawData(array, ['yellow' if x == index - 1 or x == index else 'green' for x in range(len(array))])
        time.sleep(timeTick)