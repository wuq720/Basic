"""
插入排序，平均时间复杂度O(n^2)，空间复杂度O(1)
"""


def insertsort(x):
    for i in range(len(x)-1):
        item = x[i+1]
        j = i
        while j >= 0 and item < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = item
    return x


x = [6, 4, 5, 7, 9, 2, 3, 1, 8]
print(insertsort(x))