"""
顺序表的构建需要预先知道数据大小来申请连续的存储空间，而在进行扩充时又需要进行数据的搬迁，所以使用起来并不是很灵活。
链表结构可以充分利用计算机内存空间（可以不用连续的开辟内存来保存数据），实现灵活的内存动态管理。

is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""


class SingleNode:    #单链表的节点
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:   #单链表
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index < self.length():
            node = SingleNode(item)
            pre = self._head
            for i in range(index-1):
                pre = pre.next
            node.next = pre.next
            pre.next = node
        else:
            self.append(item)

    def remove(self, item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.data == item:
                if pre is None:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.data == item:
                return True
            cur = cur.next
        return False
