"""
“双向链表”或“双面链表”
每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。

is_empty() 链表是否为空
length() 链表长度
travel() 遍历链表
add(item) 链表头部添加
append(item) 链表尾部添加
insert(pos, item) 指定位置添加
remove(item) 删除节点
search(item) 查找节点是否存在
"""


class Node: #双向链表节点
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList:    #双向链表
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
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index < self.length():
            node = Node(item)
            pre = self._head
            for i in range(index - 1):
                pre = pre.next
            node.prev = pre
            node.next = pre.next
            pre.next.prev = node
            pre.next = node
        else:
            self.append(item)

    def remove(self, item):
        cur = self._head
        while cur is not None:
            if cur.item == item:
                if cur.prev is None:
                    if cur.next is None:
                        self._head = None
                    else:
                        self._head = cur.next
                        cur.next.prev = None
                    break
                elif cur.next is None:
                    cur.prev.next = None
                    break
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
            else:
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

test = DLinkList()
test.add(1)
test.append(2)
test.append(4)
test.append(5)
test.travel()
print("is empty =", test.is_empty())
print("length =", test.length())
test.add(0)
test.travel()
test.insert(3,3)
test.travel()
test.remove(2)
test.travel()
print("6 :", test.search(6))
print("3 :", test.search(3))