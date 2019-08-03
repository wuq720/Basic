"""
冒泡排序改进，如果一次循环内没有发生交换，则表示已经排序完成
"""


def bubblesort_1(x):
    for i in range(len(x) - 1):
        flag = False
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                flag = True
        if not flag:
            return x
    return x


x = [1, 4, 7, 10, 6]
print(bubblesort_1(x))