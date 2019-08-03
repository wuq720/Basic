"""
算法简介
    二分查找（Binary Search），是一种在有序数组中查找某一特定元素的查找算法。
    查找过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则查找过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。
    这种查找算法每一次比较都使查找范围缩小一半。

复杂度分析
    时间复杂度：折半搜索每次把搜索区域减少一半，时间复杂度为 O(logn)
    空间复杂度：O(1)
"""
import numpy as np


def binarySearch(list, key):
    start = 0
    end = len(list) - 1
    while end >= start:
        mid = (start + end) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return False


LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
LIST = np.sort(LIST)
print('排序后的列表为：', LIST)
RESULT = binarySearch(LIST, 7)
print(RESULT)