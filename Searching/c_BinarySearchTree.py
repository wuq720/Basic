"""
算法简介
    二叉查找树是先对待查找的数据进行生成树，确保树的左分支的值小于右分支的值，然后在就行和每个节点的父节点比较大小，查找最适合的范围。
    这个算法的查找效率很高，但是如果使用这种查找方法要首先创建树。

算法思想
    二叉查找树（BinarySearch Tree）或者是一棵空树，或者是具有下列性质的二叉树：
　　    1）若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
　　    2）若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
　　    3）任意节点的左、右子树也分别为二叉查找树。

二叉查找树性质：对二叉查找树进行中序遍历，即可得到有序的数列。

复杂度分析
    它和二分查找一样，插入和查找的时间复杂度均为O(logn)，但是在最坏的情况下仍然会有O(n)的时间复杂度。原因在于插入和删除元素的时候，树没有保持平衡。
"""


#定义树中的节点
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    #搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        elif node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    #插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    #删除
    def delete(self, root, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            print("无该关键词")
        else:
            if n.lchild is None or n.rchild is None: #只有一个儿子，则将此节点parent的指针指向此节点的儿子，然后删除节点
                if n == p.lchild:
                    p.lchild = n.rchild if n.lchild is None else n.lchild
                    del p
                else:
                    p.rchild = n.rchild if n.lchild is None else n.lchild
                    del p
            else: #节点有两个儿子，则将其右子树的最小数据代替此节点的数据，并将其右子树的最小数据删除
                pre = n
                next = n.rchild
                while next.lchild is not None:
                    pre = next
                    next = next.lchild
                n.data = next.data
                if pre == n:
                    n.rchild = next.rchild
                else:
                    pre.lchild = next.rchild
                del p

    #先序遍历
    def pre_order_traverse(self, node):
        if node is not None:
            print(node.data)
            self.pre_order_traverse(node.lchild)
            self.pre_order_traverse(node.rchild)

    #中序遍历
    def in_order_traverse(self, node):
        if node is not None:
            self.pre_order_traverse(node.lchild)
            print(node.data)
            self.pre_order_traverse(node.rchild)

    #后序遍历
    def post_order_traverse(self, node):
        if node is not None:
            self.pre_order_traverse(node.lchild)
            self.pre_order_traverse(node.rchild)
            print(node.data)


a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)  # 创建二叉查找树
bst.pre_order_traverse(bst.root)  # 遍历

bst.delete(bst.root, 60)
print()
bst.pre_order_traverse(bst.root)



