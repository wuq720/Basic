"""
快速排序，平均时间复杂度O(nlogn)，空间复杂度O(n)，采用分治思想（Divide and Conquer）
快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。
但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，比复杂度稳定等于 O(nlogn) 的归并排序要小很多。
所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
找基准-分区-递归
"""


def quickSort(x, start=None, end=None):
    start = 0 if not isinstance(start, (int, float)) else start
    end = len(x)-1 if not isinstance(end, (int, float)) else end
    if start < end:
        partitionIndex = partition(x, start, end)
        quickSort(x, start, partitionIndex-1)
        quickSort(x, partitionIndex+1, end)
    return x


def partition(x, start, end):
    pivot = start
    index = start
    for i in range(start+1, end+1):
        if x[i] < x[pivot]:
            index += 1
            x[i], x[index] = x[index], x[i]
    x[pivot], x[index] = x[index], x[pivot]
    return index


x = [6, 4, 5, 7, 9, 2, 3, 1, 8]
print(quickSort(x))