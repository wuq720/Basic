"""
双向冒泡排序(鸡尾酒排序)，解决小元素大量存在于尾部的情况。小元素向左，大元素向右，
"""


def bidirectionbubblesort(x):
    for i in range(len(x) // 2 + 1):
        flag = False
        for j in range(i, len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                flag = True
        for j in range(len(x) - i - 1, i, -1):
            if x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]
                flag = True
        if not flag:
            return x
    return x


x = [1, 4, 5, 7, 9, 2, 3, 6, 8]
print(bidirectionbubblesort(x))