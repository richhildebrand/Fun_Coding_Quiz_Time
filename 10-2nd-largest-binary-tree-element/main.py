import sys

def findLargestElement(root):
    currentNode = root
    while currentNode:
        if currentNode.right: currentNode = currentNode.right
        else: break

    return currentNode.value

def findSecondLargestElement(root):
    if not root.left and not root.right: raise Exception("must have two nodes to find second highest value")

    secondHighestValue = None
    currentNode = root
    while currentNode:
        if currentNode.right: 
            secondHighestValue = currentNode.value
            currentNode = currentNode.right
        elif currentNode.left: 
            return findLargestElement(currentNode.left)
        else: break

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