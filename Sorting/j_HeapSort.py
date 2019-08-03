"""
堆排序, 利用堆的概念来排序的选择排序,平均时间复杂度Ο(nlogn)
"""


def buildMaxHeap(x):
    for i in range(len(x)//2-1, -1, -1):
        heapify(x, i)


def heapify(x, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < xlen and x[left] > x[largest]:
        largest = left
    if right < xlen and x[right] > x[largest]:
        largest = right
    if largest != i:
        x[i], x[largest] = x[largest], x[i]
        heapify(x, largest)


def heapSort(x):
    global xlen
    xlen = len(x)
    buildMaxHeap(x)
    for i in range(len(x)-1, 0, -1):
        x[0], x[i] = x[i], x[0]
        xlen -= 1
        heapify(x, 0)
    return x


x = [11, 6, 4, 5, 7, 9, 2, 3, 1, 8, 10]
print(heapSort(x))
