def isSuperBalanced(rootNode):
    numberOfLeaves = 0
    firstLeafValue = None
    leaves = {}

    nodes = [rootNode]
    while len(nodes):
        node = nodes.pop()

        isLeaf = not node.right and not node.left
        if isLeaf:
            print('leaf:' + str(node.value))
            isNewLeaf = leaves.get(node.value, True) 
            if isNewLeaf:
                leaves[node.value] = False
                numberOfLeaves += 1
                firstLeafValue = firstLeafValue or node.value

            if numberOfLeaves > 2: return False
            if firstLeafValue and abs(firstLeafValue-node.value) > 1: return False

        if node.right: nodes.append(node.right)
        if node.left: nodes.append(node.left)

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