def allowableDistanceExceeded(depths):
    leftDepth = depths[0]
    rightDepth = depths[1]

    return abs(leftDepth - rightDepth) > 1

def isSuperBalanced(tree):
    depths  = []
    nodes = []
    nodes.append((tree, 0))

    while len(nodes):
        node, depth = nodes.pop()

        hasLeaf = node.left or node.right
        if not hasLeaf: #is leaf
            if depth not in depths:
                depths.append(depth)

            numberOfDepths = len(depths)
            tooManyDepths = numberOfDepths > 2
            canShortCut = numberOfDepths == 2 and allowableDistanceExceeded(depths)
            if tooManyDepths or canShortCut:
                return False
        else: #not leaf
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

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