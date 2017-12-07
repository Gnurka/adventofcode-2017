import re


class Node:
    def __init__(self, root, weight, children):
        self.root = root
        self.weight = weight
        self.children = children
        #self.child_weights = []

    def __repr__(self):
        return self.root + "(" + str(self.weight) + ") -> " + str(self.children) # + ". Child weights: " + str(self.child_weights)


def open_nodes_file(file):
    with open(file) as fp:
        nodes = []
        for line in fp:
            l = re.findall('\w+', line)
            children = l[2:]
            nodes.append(Node(l[0], int(l[1]), children))

        return nodes


def star1():
    nodes = open_nodes_file('input.txt')

    print(find_root(nodes))


def find_root(nodes):
    for a in nodes:
        found = False

        for b in nodes:
            if a.root in b.children:
                found = True
                break

        if not found:
            return a


def node_weight(node):
    pass


def find_unbalanced_node(node, nodes):
    if len(node.children) == 0:
        return node.weight

    weights = []
    for i, c in enumerate(node.children):
        child = [n for n in nodes if c == n.root]
        w = find_unbalanced_node(child[0], nodes)
        weights.append(w)
        if i > 0 and w != weights[0]:
            print(child[0], weights)

    node.child_weights = weights
    return sum(weights) + node.weight


def star2():
    nodes = open_nodes_file('input.txt')
    root = find_root(nodes)
    find_unbalanced_node(root, nodes)


star1()
star2()