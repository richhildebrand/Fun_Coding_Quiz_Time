def isValidBinarySearchTree(root):
    nodes = [root]
    while len(nodes):
        parent = nodes.pop()

        if parent.left:
            if parent.left.value >= parent.value: return False
            else: nodes.append(parent.left)
        if parent.right:
            if parent.right.value <= parent.value: return False
            else: nodes.append(parent.right)

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