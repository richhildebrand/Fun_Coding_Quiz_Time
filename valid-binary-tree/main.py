import sys

def isValidBinarySearchTree(root):
    nodeContainers = [(root, -sys.maxsize-1, sys.maxsize)]
    while len(nodeContainers):
        node, minValue, maxValue = nodeContainers.pop()

        print('value:' + str(node.value) + '   min:'+ str(minValue) + '   max:' + str(maxValue))
        if node.left:
            if node.left.value <= minValue \
            or node.left.value >= maxValue:
                return False
            else:
                newContainer = (node.left, minValue, node.value)
                nodeContainers.append(newContainer)
        if node.right:
            if node.right.value <= minValue \
            or node.right.value >= maxValue:
                return False
            else: 
                newContainer = (node.right, node.value, maxValue)
                nodeContainers.append(newContainer)

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