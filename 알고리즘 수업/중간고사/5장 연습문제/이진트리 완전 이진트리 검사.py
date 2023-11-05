class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def isLeaf(self):
        return (self.left == None and self.right == None)

def count_node(root):
    if root is None:
        return 0
    left = count_node(root.left)
    right = count_node(root.right)
    return left + right + 1


def checkNumber(n, id, max):
    if n == None:
        return 1
    if id > max:
        return 0
    if n.left != None and checkNumber(n.left, id * 2, max) == 0:
        return 0
    if n.right != None and checkNumber(n.right, id * 2 + 1, max) == 0:
        return 0
    return 1

g = TNode('G', None, None)
f = TNode('F', None, None)
d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
c = TNode('C', g, f)
a = TNode('A', b, c)

def is_complete_binary_tree(root):
    nNodes = count_node(root)
    # nNodes = max
    ret = checkNumber(root, 1, nNodes)
    if ret == 0:
        return False
    else:
        return True

print(is_complete_binary_tree(a))