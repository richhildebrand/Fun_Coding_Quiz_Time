import unittest
import main as main


class AlgorithmShould(unittest.TestCase):
    def test_smoke(self):
        root = main.BinaryTreeNode(0)
        result = main.isValidBinarySearchTree(root)
        self.assertTrue(result)

    def test_returnTrue_whenNodesBalance(self):
        root = main.BinaryTreeNode(10)
        left1 = root.insert_left(5)
        left1.insert_left(1)
        left1.insert_right(7)

        right1 = root.insert_right(15)
        right1.insert_left(12)
        right2 = right1.insert_right(20)
        right2.insert_right(22)

        result = main.isValidBinarySearchTree(root)
        self.assertTrue(result)

    def test_returnFalse_withHigherLeftNode(self):
        root = main.BinaryTreeNode(10)
        left1 = root.insert_left(5)
        left1.insert_left(1)
        left1.insert_right(7)

        right1 = root.insert_right(15)
        right1.insert_left(12)
        right2 = right1.insert_right(20)
        right2.insert_right(22)

        result = main.isValidBinarySearchTree(root)
        self.assertFalse(result)

    def test_returnFalse_withRightBranchLowerThanRoot(self):
        root = main.BinaryTreeNode(10)
        left1 = root.insert_left(5)
        left1.insert_left(1)
        left1.insert_right(7)

        right1 = root.insert_right(15)
        right1.insert_left(9)
        right1.insert_right(17)

        result = main.isValidBinarySearchTree(root)
        self.assertFalse(result)

    def test_returnFalse_withLeftBranchHigherThanRoot(self):
        root = main.BinaryTreeNode(10)
        left1 = root.insert_left(5)
        left1.insert_left(1)
        left1.insert_right(12)

        right1 = root.insert_right(15)
        right1.insert_left(12)
        right1.insert_right(15)

        result = main.isValidBinarySearchTree(root)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)