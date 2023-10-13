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

def post_order(root):
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=' ')

post_order(root)