"""
递归解决方案的优点是它更容易实现。
但是，存在一个很大的缺点：如果递归的深度太高，你将遭受堆栈溢出。
在这种情况下，您可能会希望使用 BFS，或使用显式栈实现 DFS。
"""
class Node:
    def __init__(self):
        self.neighbor = []

    def addNeighbor(self, node):
        self.neighbor.append(node)


def DFS(root: Node, target: Node):
    visited, s = set(), [root]
    while s:
        cur = s.pop()
        if cur == target:
            return True
        for nxt in cur.neighbor:
            if nxt not in visited:
                s.append(nxt)
                visited.add(nxt)
    return False
