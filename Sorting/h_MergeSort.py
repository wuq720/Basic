"""
归并排序，平均时间复杂度O(nlogn)，空间复杂度O(n)，采用分治思想（Divide and Conquer）
"""


def mergeSort(x):
    if len(x) < 2:
        return x
    middle = len(x) // 2
    left = mergeSort(x[:middle])
    right = mergeSort(x[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    while left:
        result.append(left[0])
        left.pop(0)
    while right:
        result.append(right[0])
        right.pop(0)
    return result


x = [6, 4, 5, 7, 9, 2, 3, 1, 8]
print(mergeSort(x))
