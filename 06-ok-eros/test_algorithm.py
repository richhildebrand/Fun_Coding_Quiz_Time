import unittest
import round2 as main


class AlgorithmShould(unittest.TestCase):
    def test_returnEmpty_WithX1_tooHigh(self):
        rectangleOne = self.makeRectangle(10, 1, 6, 3)
        rectangleTwo = self.makeRectangle(5, 2, 3, 6)

        result = main.findIntersection(rectangleOne, rectangleTwo)

        expectedRectangle = {}
        self.assertDictEqual(result, expectedRectangle)

    def test_returnEmpty_WithX2_tooHigh(self):
        rectangleOne = self.makeRectangle(10, 1, 6, 3)
        rectangleTwo = self.makeRectangle(22, 2, 3, 6)

        result = main.findIntersection(rectangleOne, rectangleTwo)

        expectedRectangle = {}
        self.assertDictEqual(result, expectedRectangle)

    def test_returnEmpty_WithY1_tooHigh(self):
        rectangleOne = self.makeRectangle(10, 11, 6, 3)
        rectangleTwo = self.makeRectangle(5, 2, 3, 6)

        result = main.findIntersection(rectangleOne, rectangleTwo)

        expectedRectangle = {}
        self.assertDictEqual(result, expectedRectangle)

    def test_returnEmpty_WithY2_tooHigh(self):
        rectangleOne = self.makeRectangle(10, 1, 6, 3)
        rectangleTwo = self.makeRectangle(5, 21, 3, 6)

        result = main.findIntersection(rectangleOne, rectangleTwo)

        expectedRectangle = {}
        self.assertDictEqual(result, expectedRectangle)

    def test_findIntesection(self):
        rectangleOne = self.makeRectangle(1, 1, 6, 3)
        rectangleTwo = self.makeRectangle(5, 2, 3, 6)

        result = main.findIntersection(rectangleOne, rectangleTwo)

        expectedRectangle = self.makeRectangle(5, 2, 2, 2)
        self.assertDictEqual(result, expectedRectangle)

    def makeRectangle(self, x, y, width, height):
        return {
            # Coordinates of bottom-left corner
            'left_x'   : x,
            'bottom_y' : y,

            # Width and height
            'width'    : width,
            'height'   : height,
        }


if __name__ == '__main__':
    unittest.main(verbosity=2)