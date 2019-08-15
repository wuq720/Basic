"""
深度优先搜索算法（Depth-First-Search，缩写为 DFS），是一种利用递归实现的搜索算法。
DFS 用于找所有解的问题，它的空间效率高，而且找到的不一定是最优解，必须记录并完成整个搜索
"""


class Node:
    def __init__(self):
        self.neighbor = []

    def addNeighbor(self, node):
        self.neighbor.append(node)


def DFS(cur: Node, target: Node, visited: set[Node]):
    if cur == target:
        return True
    for nxt in cur.neighbor:
        if nxt not in visited:
            visited.add(nxt)
            if DFS(nxt, target, visited):
                return True
    return False