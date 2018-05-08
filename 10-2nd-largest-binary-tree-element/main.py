def findSecondLargestElement(root):
    keepLooking = True
    secondHighestValue = None
    currentNode = root
    while keepLooking:

        if currentNode.right:
            keepLooking = True
            secondHighestValue = currentNode.value
            currentNode = currentNode.right
            continue
        else: keepLooking = False

    return secondHighestValue

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