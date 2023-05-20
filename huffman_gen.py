from collections import defaultdict
import heapq

class Node:
    def __init__(self, symbol, frequency, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def calculate_frequency(data):
    frequency = defaultdict(int)
    for i in range(len(data) - 7):
        pattern = data[i:i+8]
        frequency[pattern] += 1
    return frequency

def build_huffman_tree(frequency):
    heap = []
    for pattern, freq in frequency.items():
        heapq.heappush(heap, Node(pattern, freq))

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.frequency + node2.frequency, node1, node2)
        heapq.heappush(heap, merged)

    return heap[0]

def assign_codes(node, code='', codes={}):
    if node.symbol:
        codes[node.symbol] = code
    else:
        assign_codes(node.left, code + '0', codes)
        assign_codes(node.right, code + '1', codes)

    return codes

def encode_data(data, codes):
    encoded_data = ''
    i = 0
    while i < len(data) - 7:
        pattern = data[i:i+8]
        if pattern in codes:
            encoded_data += codes[pattern]
            i += 8
        else:
            encoded_data += pattern
            i += 1
    return encoded_data

def compress_binary_data(data):
    frequency = calculate_frequency(data)
    huffman_tree = build_huffman_tree(frequency)
    codes = assign_codes(huffman_tree)
    encoded_data = encode_data(data, codes)
    return encoded_data

