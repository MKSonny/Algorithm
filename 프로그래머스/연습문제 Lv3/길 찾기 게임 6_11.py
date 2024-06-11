import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def solution(nodeinfo):
    sys.setrecursionlimit(10000)

    answer = [[] for _ in range(2)]

    def preorder(node, answer):
        if node:
            answer[0].append(node.data[2])
            # print(node.data[2], end=' ')
            preorder(node.left, answer)
            preorder(node.right, answer)

    def postorder(node, answer):
        if node:
            postorder(node.left, answer)
            postorder(node.right, answer)
            answer[1].append(node.data[2])
            # print(node.data[2], end=' ')

    for idx, i in enumerate(nodeinfo):
        i.append(idx + 1)

    nodeinfo.sort(key=lambda o: (o[1], -o[0]), reverse=True)

    root = Node((nodeinfo[0][1], nodeinfo[0][0], nodeinfo[0][2]))

    def dfs(y, x, root, node):
        # if root == None:
        #     return
        ry, rx, num = root.data
        if y < ry:
            if x < rx:
                if root.left != None:
                    dfs(y, x, root.left, node)
                else:
                    root.left = node
                    return
            else:
                if root.right != None:
                    dfs(y, x, root.right, node)
                else:
                    root.right = node
                    return
        else:
            if x < rx:
                root.left = node
            else:
                root.right = node

    for i in range(1, len(nodeinfo)):
        x, y, num = nodeinfo[i]
        dfs(y, x, root, Node((y, x, num)))

    preorder(root, answer)
    # print()
    postorder(root, answer)

    return answer