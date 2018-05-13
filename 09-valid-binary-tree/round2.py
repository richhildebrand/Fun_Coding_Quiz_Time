import sys

def appendNode(nodes, nodeToAppend, minValue, maxValue):
    newCollection = (nodeToAppend, minValue, maxValue)
    nodes.append(newCollection)
    return

def isValidBinarySearchTree(rootNode):

    nodes = [(rootNode, -sys.maxsize-1, sys.maxsize)]
    while len(nodes):
        node, minValue, maxValue = nodes.pop()
        if minValue > node.value or node.value > maxValue: return False
        print('minValue:' + str(minValue) + '   node.value:' + str(node.value) + '   maxValue:' + str(maxValue))

        if node.right:
            appendNode(nodes, node.right, node.value, maxValue)
        if node.left:
            appendNode(nodes, node.left, minValue, node.value)

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