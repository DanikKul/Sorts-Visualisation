import time


def shell_sort(array, drawData, timeTick):
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                drawData(array, ['yellow' if x == j or x == j - interval else 'green' for x in range(len(array))])
                time.sleep(timeTick)

            array[j] = temp
        interval //= 2
