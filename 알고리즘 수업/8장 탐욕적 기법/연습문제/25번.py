import heapq

val = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
freq = [24, 3, 8, 10, 33, 6, 4, 12]

# 디코딩 구현 방법?

'''
label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
freq = [24, 3, 8, 10, 33, 6, 4, 12]
'''

def build_huffman_tree(val, freq):
    n = len(val)
    h = []

    for i in range(n):
        heapq.heappush(h, (freq[i], val[i], Node(val[i])))

    while len(h) > 1:
        e1 = heapq.heappop(h)
        e2 = heapq.heappop(h)

        combined_node = Node(e1[1] + e2[1])
        combined_node.left = e1[2]
        combined_node.right = e2[2]

        heapq.heappush(h, (e1[0] + e2[0], e1[1] + e2[1], combined_node))

    return h[0][2]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_huffman_codes(root, code="", mapping={}):
    if root is not None:
        if root.value.isalpha():
            mapping[root.value] = code
        generate_huffman_codes(root.left, code + "0", mapping)
        generate_huffman_codes(root.right, code + "1", mapping)
    return mapping

def huffman(val, freq):
    root = build_huffman_tree(val, freq)
    huffman_codes = generate_huffman_codes(root)
    return huffman_codes

huffman_codes = huffman(val, freq)
print("Huffman Codes:")
for symbol, code in huffman_codes.items():
    print(f"{symbol}: {code}")
