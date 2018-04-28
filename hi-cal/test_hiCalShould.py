import unittest as unittest
import main as main


class HiCalShould(unittest.TestCase):
    def test_returnTrue(self):
        assert main.returnTrue()


if __name__ == '__main__':
    unittest.main(verbosity=2)