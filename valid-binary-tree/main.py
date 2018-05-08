import sys

def isValidBinarySearchTree(root):
    nodeContainers = [{ 'node': root, 'min': -sys.maxsize-1, 'max': sys.maxsize }]
    while len(nodeContainers):
        nodeContainer = nodeContainers.pop()
        node = nodeContainer['node']

        print('value:' + str(node.value) + '   min:'+ str(nodeContainer['min']) + '   max:' + str(nodeContainer['max']))
        if node.left:
            if node.left.value >= node.value \
            or node.left.value >= nodeContainer['max'] \
            or node.left.value <= nodeContainer['min']:
                return False
            else:
                newContainer = { 'node': node.left, 'min': nodeContainer['min'], 'max': node.value }
                nodeContainers.append(newContainer)
        if node.right:
            if node.right.value <= node.value \
            or node.right.value <= nodeContainer['min'] \
            or node.right.value >= nodeContainer['max']:
                return False
            else: 
                newContainer = { 'node': node.right, 'min': node.value, 'max': nodeContainer['max'] }
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