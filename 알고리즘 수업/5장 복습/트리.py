class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


l = TNode('L', None, None)
k = TNode('K', None, None)
j = TNode('J', None, None)
i = TNode('I', None, None)
h = TNode('H', k, l)
g = TNode('G', None, None)
f = TNode('F', None, j)
e = TNode('E', None, i)
d = TNode('D', g, h)
c = TNode('C', e, f)
b = TNode('B', c, d)
a = TNode('A', b, None)

def calc_height(root):
    if root is None:
        return 0
    left = calc_height(root.left)
    right = calc_height(root.right)
    return max(left, right) + 1

def preorder(root):
    if root is not None:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end = ' ')
        inorder(root.right)

print(calc_height(a))
inorder(a)