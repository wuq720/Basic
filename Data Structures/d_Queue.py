"""
队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
先进先出FIFO

Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty():
        return bool(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.__dict__)
print(q.dequeue())
print(q.dequeue())