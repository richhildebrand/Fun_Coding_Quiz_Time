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

    def test_findWithOnly_LeftBranches(self):
        root = main.BinaryTreeNode(10)
        left1 = root.insert_left(9)
        left2 = left1.insert_left(8)
        left2.insert_left(7)

        result = main.findSecondLargestElement(root)
        self.assertEquals(result, 9)


if __name__ == '__main__':
    unittest.main(verbosity=2)