def traverseBranch(node, currentDepth, maxDepth): 
    currentDepth += 1
    maxDepth = max(currentDepth, maxDepth)
    if (node.left != None):
        leftDepth = traverseBranch(node.left, currentDepth, maxDepth)
        maxDepth = max(leftDepth, maxDepth)
    if (node.right != None):
        rightDepth = traverseBranch(node.right, currentDepth, maxDepth)
        maxDepth = max(rightDepth, maxDepth)

    return maxDepth

def isSuperBalanced(tree):
    leftDepth = traverseBranch(tree.left, 0, 0)
    print('leftDepth:' + str(leftDepth))
    rightDepth = traverseBranch(tree.right, 0, 0)
    print('rightDepth:' + str(rightDepth))

    return abs(leftDepth - rightDepth) <= 1


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