from unittest import TestCase

import numpy as np
from distances import euclidean


class TestEuclidean(TestCase):
    a1 = np.array([1, 2, 3, 5, 6, 9])
    a2 = np.array([a1, a1])
    a3 = np.array([5, 5, 5, 5, 5, 5])
    a4 = np.array([a3, a3])
    a5 = np.array([3, 3, 3, 3, 3, 3])
    a6 = np.array([a1, a3, a5])

    def test_point_distance(self):
        """Test that distance from a single point is computed correctly."""
        real = euclidean.euclidean_from_point(self.a1, self.a3)
        self.assertAlmostEqual(real, 6.782329983125268, 6)

        real = euclidean.euclidean_from_point(self.a2, self.a3)
        exp = np.array([6.782329983125268, 6.782329983125268])
        np.testing.assert_allclose(real, exp, rtol=1e-6, atol=1e-6)

        real = euclidean.euclidean_from_point(self.a3, np.array([5]))
        exp = np.array([0, 0, 0, 0, 0, 0])
        np.testing.assert_array_equal(real, exp)

    def test_points_distance(self):
        """Test that distance from multiple points is computed correctly."""
        real = euclidean.euclidean_from_points(self.a1, self.a4)
        exp = np.array([[6.782329983125268, 6.782329983125268]])
        np.testing.assert_allclose(real, exp, rtol=1e-6, atol=1e-6)

        real = euclidean.euclidean_from_points(self.a2, self.a4)
        exp = np.array(
            [
                [6.782329983125268, 6.782329983125268],
                [6.782329983125268, 6.782329983125268],
            ]
        )
        np.testing.assert_allclose(real, exp, rtol=1e-6, atol=1e-6)

    def test_distance_from_center(self):
        """Test that the distance from center is computed correctly."""
        real = euclidean.euclidean_from_center(self.a6)
        exp = np.array([4.422166387140533, 3.0912061651652345, 3.4960294939005054])
        np.testing.assert_allclose(real, exp, rtol=1e-6, atol=1e-6)

        # TO UNDERSTAND WHAT TO DO WITH 1D ARRAY
        real = euclidean.euclidean_from_center(self.a1)
        exp = np.array([0])
        np.testing.assert_array_equal(real, exp)
