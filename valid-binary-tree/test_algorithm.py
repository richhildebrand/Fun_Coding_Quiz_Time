import unittest
import main as main


class AlgorithmShould(unittest.TestCase):
    def test_smoke(self):
        root = main.BinaryTreeNode(0)
        result = main.isValidBinarySearchTree(root)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)