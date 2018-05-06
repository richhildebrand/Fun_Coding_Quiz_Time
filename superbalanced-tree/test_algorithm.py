import unittest
import main as main


class AlgorithmShould(unittest.TestCase):
    def test_oneBranch_OnEachSide(self):
        trunk = main.BinaryTreeNode(15)
        trunk.insert_left(7)
        trunk.insert_right(11)

        isSuperBalanced = main.isSuperBalanced(trunk)
        self.assertTrue(isSuperBalanced)

    def test_two_toOne(self):
        trunk = main.BinaryTreeNode(15)
        left = trunk.insert_left(7)
        left.insert_right(3)

        trunk.insert_right(11)

        isSuperBalanced = main.isSuperBalanced(trunk)
        self.assertTrue(isSuperBalanced)
    
    def test_one_toTwo(self):
        trunk = main.BinaryTreeNode(15)
        trunk.insert_left(7)

        right = trunk.insert_right(11)
        right = right.insert_left(4)

        isSuperBalanced = main.isSuperBalanced(trunk)
        self.assertTrue(isSuperBalanced)

    def test_five_toThree(self):
        trunk = main.BinaryTreeNode(0)
        left1 = trunk.insert_left(1)
        left2 = left1.insert_right(2)
        left1.insert_left(2)
        left3 = left2.insert_right(3)
        left4 = left3.insert_right(4)
        left5 = left4.insert_left(4)

        right1 = trunk.insert_right(1)
        right2 = right1.insert_left(2)
        right2.insert_right(3)
        right2.insert_left(3)

        isSuperBalanced = main.isSuperBalanced(trunk)
        self.assertFalse(isSuperBalanced)


if __name__ == '__main__':
    unittest.main(verbosity=2)