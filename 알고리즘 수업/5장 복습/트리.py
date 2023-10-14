class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

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

print(calc_height(root))
preorder(root)