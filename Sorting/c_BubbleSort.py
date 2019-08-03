"""
冒泡排序，平均时间复杂度O(n^2)，空间复杂度O(1)
"""

def bubblesort(x):
    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


x=[1, 4, 7, 10, 6]
print(bubblesort(x))
