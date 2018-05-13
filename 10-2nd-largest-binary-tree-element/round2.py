def findLargestElement(rootNode):
    node = rootNode
    while node:
        if node.right: node = node.right
        else: return node.value

def findSecondLargestElement(rootNode):
    if not (rootNode.left or rootNode.right): raise ValueError("must have at least two nodes") 

    secondLargetsValue = rootNode.value
    node = rootNode
    while node:
        if node.right: 
            secondLargetsValue = node.value
            node = node.right
        elif node.left: return findLargestElement(node.left)
        else: return secondLargetsValue

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right