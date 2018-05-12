def isSuperBalanced(rootNode):
    numberOfLeaves = 0
    firstDepth = None
    depths = {}

    nodes = [(rootNode, 0)]
    while len(nodes):
        node, depth = nodes.pop()

        isLeaf = not node.right and not node.left
        if isLeaf:
            print('leaf:' + str(node.value))
            isNewDepth = depths.get(depth, True)
            if isNewDepth:
                depths[depth] = False
                numberOfLeaves += 1
                firstDepth = firstDepth or depth

            if numberOfLeaves > 2: return False
            if firstDepth and abs(firstDepth-depth) > 1: return False

        if node.right: nodes.append((node.right, depth+1))
        if node.left: nodes.append((node.left, depth+1))

    return True


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right