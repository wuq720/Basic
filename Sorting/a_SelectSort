"""
选择排序，平均时间复杂度O(n^2)，空间复杂度O(1)
"""


def selectsort(x):
    for i in range(0, len(x)-1):
        minindex = i
        for j in range(i+1, len(x)):
            if x[j] < x[minindex]:
                minindex = j
        x[minindex], x[i] = x[i], x[minindex]
    return x


print(selectsort([1, 4, 5, 3, 6]))
