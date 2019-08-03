"""
算法简介
    顺序查找又称为线性查找，是一种最简单的查找方法。适用于线性表的顺序存储结构和链式存储结构。该算法的时间复杂度为O(n)。

基本思路
    从第一个元素m开始逐个与需要查找的元素x进行比较，当比较到元素值相同(即m=x)时返回元素m的下标，如果比较到最后都没有找到，则返回-1。

优缺点
    缺点：是当n 很大时，平均查找长度较大，效率低；
    优点：是对表中数据元素的存储没有要求。另外，对于线性链表，只能进行顺序查找。
"""


def sequentialSearch(list, key):
    result = False
    for i in range(len(list)):
        if list[i] == key:
            result = i
    return result


LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
RESULT = sequentialSearch(LIST, 5)
print(RESULT)
