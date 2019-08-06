"""
广度优先搜索算法（Breadth-First-Search，缩写为 BFS），是一种利用队列实现的搜索算法。
应用：1）遍历 2）找出最短路径
常用于找单一的最短路线，它的特点是 "搜到就是最优解"
"""


# class Graph:    # 使用邻接表
#     def __init__(self, numvertex):
#         self._numVertex = numvertex
#         self._adj = [[] for _ in range(numvertex)]
#
#     def add_edge(self, s, t):
#         self._adj[s].append(t)


from queue import Queue


class Node:
    def __init__(self):
        self.neighbor = []

    def addNeighbor(self, node):
        self.neighbor.append(node)


def BFS(root: Node, target: Node):
    queue = Queue()
    used = set()
    step = 0
    queue.put(root)
    used.add(root)
    while not queue.empty():
        step += 1
        size = queue.qsize()
        for i in range(size):
            cur = queue.get()
            if cur == target:
                return step
            nex = cur.neighbor
            for n in nex:
                if n not in used:
                    queue.put(n)
                    used.add(n)
    return -1


a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()
a.addNeighbor(b)
a.addNeighbor(c)
a.addNeighbor(d)
b.addNeighbor(e)
c.addNeighbor(e)
c.addNeighbor(f)
d.addNeighbor(g)
f.addNeighbor(g)

step = BFS(a, g)
print(step)


