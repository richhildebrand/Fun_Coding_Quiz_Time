import unittest
import main as main


class AlgorithmShould(unittest.TestCase):
    def test_findWithOnly_RightBranches(self):
        root = main.BinaryTreeNode(10)
        right1 = root.insert_right(15)
        right2 = right1.insert_right(22)
        right2.insert_right(25)

        result = main.findSecondLargestElement(root)
        self.assertEquals(result, 22)


if __name__ == '__main__':
    unittest.main(verbosity=2)