"""
二元选择排序，选择排序的改进
"""


def selectsort_1(x):
    for i in range(0, len(x) // 2):
        minindex = i
        maxindex = i
        for j in range(i+1, len(x)-i):
            if x[j] < x[minindex]:
                minindex = j
            if x[j] > x[maxindex]:
                maxindex = j
        if x[minindex] == x[maxindex]:
            return x
        x[minindex], x[i] = x[i], x[minindex]
        if maxindex != i:
            x[maxindex], x[len(x) - i - 1] = x[len(x) - i - 1], x[maxindex]
        else:
            x[minindex], x[len(x) - i - 1] = x[len(x) - i - 1], x[minindex]
    return x


print(selectsort_1([1, 4, 7, 9, 6]))