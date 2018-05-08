import sys

def findSecondLargestElement(root):
    if not root.left and not root.right: raise Exception("must have two nodes to find second highest value")

    highestValue = -sys.maxsize-1
    secondHighestValue = -sys.maxsize-1
    currentNode = root
    while currentNode:
        if currentNode.value >= highestValue:
            secondHighestValue = highestValue
            highestValue = currentNode.value
        elif currentNode.value > secondHighestValue:
            secondHighestValue = currentNode.value

        currentNode = currentNode.right or currentNode.left

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