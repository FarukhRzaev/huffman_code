import heapq
from collections import Counter, namedtuple


# the internal node of the binary tree
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


# binary tree leaf
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # if the specified string s is a single character


def haffman_encode(s):
    bin_tree = []
    for ch, freq in Counter(s).items():
        bin_tree.append((freq, len(bin_tree), Leaf(ch)))
    heapq.heapify(bin_tree)  # created a binary tree

    count = len(bin_tree)
    while len(bin_tree) > 1:
        freq1, _count1, left = heapq.heappop(bin_tree)
        freq2, _count2, right = heapq.heappop(bin_tree)
        heapq.heappush(bin_tree, (freq1 + freq2, count, Node(left, right)))
        count += 1
    # added a second unique tuple element so that there are no errors when comparing

    [(_freq, _count, root)] = bin_tree  # the root of the constructed tree
    code = {}
    root.walk(code, acc="")
    return code


def main():
    s = input()
    code = haffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f"{ch}: {code[ch]}")
    print(encoded)


if __name__ == "__main__":
    main()
