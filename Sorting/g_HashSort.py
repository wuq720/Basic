"""
希尔算法，插入排序的改进，对每个gap进行插入排序，平均时间复杂度O(nlogn)，空间复杂度O(1)
"""


def hashsort(x):
    gap = round(len(x)*2/3)
    while gap > 0:
        print('gap = ', gap)
        for i in range(gap-1, len(x)-1):
            item = x[i+1]
            j = i - gap + 1
            while j >= 0 and item < x[j]:
                x[j + gap] = x[j]
                j -= gap
            x[j + gap] = item
        gap = round(gap/3)
    return x


x = [6, 4, 5, 7, 9, 2, 3, 1, 8]
print(hashsort(x))