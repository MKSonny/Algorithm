def count_node(root):
    if root is None:
        return 0
    left = count_node(root.left)
    right = count_node(root.right)
    return left + right + 1

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def isLeaf(self):
        return (self.left == None and self.right == None)


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
c = TNode('C', None, None)
a = TNode('A', b, c)

def count_leaf(root):
    if root is None: return 0
    elif root.isLeaf(): return 1
    else: return count_leaf(root.left) + count_leaf(root.right)


print(count_leaf(a))