class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

a = TNode('A', None, None)
b = TNode('B', None, None)
c = TNode('/', a, b)
d = TNode('C', None, None)
e = TNode('*', c, d)
f = TNode('D', None, None)
g = TNode('*', e, f)
h = TNode('E', None, None)
root = TNode('+', g, h)

def node_count(root):
    if root is None:
        return 0
    else:
        left_cnt = node_count(root.left)
        right_cnt = node_count(root.right)
        return 1 + left_cnt + right_cnt

print(node_count(root))
