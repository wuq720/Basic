"""
栈,一种容器，可存入数据元素、访问元素、删除元素，它的特点在于只能允许在容器的一端（称为栈顶端指标，top）进行加入数据（push）和输出数据（pop）的运算。
后进先出LIFO
注意：栈和队列研究的是操作层面，顺序表和链表研究的是数据怎么存放。
栈可以用顺序表实现，也可以用链表实现.

Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
top() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            raise LookupError('stack is empty!')

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.pop()
stack.push("hello")
stack.push("world")
stack.push("!")
print(stack.size())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.size())