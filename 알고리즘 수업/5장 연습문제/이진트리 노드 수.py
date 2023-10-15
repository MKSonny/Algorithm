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


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
c = TNode('C', None, None)
a = TNode('A', b, c)

print(count_node(a))

