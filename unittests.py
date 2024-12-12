import unittest
from geometry import *
import math

phi = (math.sqrt(5) + 1) / 2


class GeometryTestCase(unittest.TestCase):
    def test_circle_perimeter_int(self):
        result = circle.perimeter(5)
        self.assertEqual(result, 10 * math.pi)

    def test_circle_area_int(self):
        result = circle.area(12)
        self.assertEqual(result, 144 * math.pi)

    def test_rectangle_perimeter_int(self):
        result = rectangle.perimeter(4, 5)
        self.assertEqual(result, 18)

    def test_rectangle_area_int(self):
        result = rectangle.area(20, 12)
        self.assertEqual(result, 240)

    def test_square_perimeter_int(self):
        result = square.perimeter(1221)
        self.assertEqual(result, 4884)

    def test_square_area_int(self):
        result = square.area(121)
        self.assertEqual(result, 14641)

    def test_triangle_perimeter_int(self):
        result = triangle.perimeter(1, 2, 4)
        self.assertEqual(result, 7)

    def test_triangle_area_int(self):
        result = triangle.area(1, 2)
        self.assertEqual(result, 1)

    def test_circle_perimeter_zero(self):
        result = circle.perimeter(0)
        self.assertEqual(result, 0)

    def test_circle_area_zero(self):
        result = circle.area(0)
        self.assertEqual(result, 0)

    def test_rectangle_perimeter_zero_1(self):
        result = rectangle.perimeter(0, 5)
        self.assertEqual(result, 10)

    def test_rectangle_perimeter_zero_2(self):
        result = rectangle.perimeter(0, 0)
        self.assertEqual(result, 0)

    def test_rectangle_area_zero_1(self):
        result = rectangle.area(0, 52)
        self.assertEqual(result, 0)     # Correct value 52 -> 0

    def test_rectangle_area_zero_2(self):
        result = rectangle.area(0, 0)
        self.assertEqual(result, 0)

    def test_square_perimeter_zero(self):
        result = square.perimeter(0)
        self.assertEqual(result, 0)

    def test_square_area_zero(self):
        result = square.area(0)
        self.assertEqual(result, 0)

    def test_triangle_perimeter_zero_1(self):
        result = triangle.perimeter(0, 12, 12)
        self.assertEqual(result, 24)

    def test_triangle_perimeter_zero_2(self):
        result = triangle.perimeter(0, 12, 24)
        self.assertEqual(result, 36)

    def test_triangle_perimeter_zero_3(self):
        result = triangle.perimeter(0, 0, 1)
        self.assertEqual(result, 1)

    def test_triangle_perimeter_zero_4(self):
        result = triangle.perimeter(0, 0, 0)
        self.assertEqual(result, 0)

    def test_triangle_area_zero_1(self):
        result = triangle.area(0, 52)
        self.assertEqual(result, 0)

    def test_triangle_area_zero_2(self):
        result = triangle.area(0, 0)
        self.assertEqual(result, 0)

    def test_circle_perimeter_float(self):
        result = circle.perimeter(math.e)
        self.assertEqual(result, math.e * 2 * math.pi)

    def test_circle_area_float(self):
        result = circle.area(math.cos(math.e))
        self.assertEqual(round(result, 3), round(math.cos(math.e) ** 2 * math.pi, 3))   # Added inaccuracy

    def test_rectangle_perimeter_float(self):
        result = rectangle.perimeter(math.e, math.pi)
        self.assertEqual(result, (math.e + math.pi) * 2)

    def test_rectangle_area_float(self):
        result = rectangle.area(math.cos(math.e), math.sqrt(math.pi))
        self.assertEqual(result, math.cos(math.e) * math.sqrt(math.pi))

    def test_square_perimeter_float(self):
        result = square.perimeter(math.e)
        self.assertEqual(result, math.e * 4)

    def test_square_area_float(self):
        result = square.area(math.cos(math.e))
        self.assertEqual(result, math.cos(math.e) ** 2)

    def test_triangle_perimeter_float(self):
        result = triangle.perimeter(math.e, math.pi, phi)
        self.assertEqual(result, math.e + math.pi + phi)

    def test_triangle_area_float(self):
        result = triangle.area(math.e, math.pi)
        self.assertEqual(result, math.e * math.pi / 2)
