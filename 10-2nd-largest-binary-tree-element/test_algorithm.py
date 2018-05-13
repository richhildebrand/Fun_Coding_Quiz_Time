import unittest
import round2 as main


class AlgorithmShould(unittest.TestCase):
    def test_throw_withOnlyRootNote(self):
        root = main.BinaryTreeNode(1)
        with self.assertRaises(Exception):
            result = main.findSecondLargestElement(root)

    def test_findWithOnly_OneLeftLeaf(self):
        root = main.BinaryTreeNode(1)
        root.insert_left(0)

        result = main.findSecondLargestElement(root)
        self.assertEqual(result, 0)

    def test_findWithOnly_OneRightLeaf(self):
        root = main.BinaryTreeNode(1)
        root.insert_right(2)

        result = main.findSecondLargestElement(root)
        self.assertEqual(result, 1)

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

    def test_findWith_secondHighest_onRightLeaf(self):
        root = main.BinaryTreeNode(15)
        left1 = root.insert_left(8)
        left1.insert_right(10)
        left2 = left1.insert_left(6)
        left2.insert_left(5)

        result = main.findSecondLargestElement(root)
        self.assertEquals(result, 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)