"""
Test suite for geometric mapping implementation.

Tests verify that the Δ¹ ring geometry mapping is:
- Deterministic
- Reversible
- Correctly computes all geometric properties
"""

import math
import unittest
from geometric_mapping import Delta1RingGeometry, GeometricCoordinate


class TestDelta1RingGeometry(unittest.TestCase):
    """Test cases for Δ¹ ring geometry operations"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.geometry = Delta1RingGeometry(ring_size=360)
    
    def test_map_1981_properties(self):
        """Test that 1981 maps to correct geometric properties"""
        coord = self.geometry.map_number_to_geometry(1981)
        
        # Verify cell index
        self.assertEqual(coord.cell_index, 181)
        
        # Verify normal vector is unit length
        magnitude = math.sqrt(coord.normal_vector[0]**2 + coord.normal_vector[1]**2)
        self.assertAlmostEqual(magnitude, 1.0, places=10)
        
        # Verify angular frequency
        self.assertAlmostEqual(coord.angular_frequency, 1981 / 360, places=10)
        
        # Verify antipode state (opposite side of ring)
        self.assertEqual(coord.antipode_state, 1)
        
        # Verify original value stored
        self.assertEqual(coord.original_value, 1981)
    
    def test_round_trip_1981(self):
        """Test that 1981 can be recovered from its geometric representation"""
        original = 1981
        coord = self.geometry.map_number_to_geometry(original)
        recovered = self.geometry.recover_from_geometry(coord)
        
        self.assertEqual(recovered, original)
    
    def test_round_trip_verify_method(self):
        """Test the verify_round_trip method for 1981"""
        self.assertTrue(self.geometry.verify_round_trip(1981))
    
    def test_deterministic_mapping(self):
        """Test that mapping is deterministic (same input -> same output)"""
        coord1 = self.geometry.map_number_to_geometry(1981)
        coord2 = self.geometry.map_number_to_geometry(1981)
        
        self.assertEqual(coord1.cell_index, coord2.cell_index)
        self.assertEqual(coord1.normal_vector, coord2.normal_vector)
        self.assertEqual(coord1.angular_frequency, coord2.angular_frequency)
        self.assertEqual(coord1.antipode_state, coord2.antipode_state)
    
    def test_normal_vector_direction(self):
        """Test that normal vector points in correct direction"""
        coord = self.geometry.map_number_to_geometry(1981)
        
        # Cell index 181 should be at angle (181 * 2π / 360)
        expected_theta = (2 * math.pi * 181) / 360
        expected_x = math.cos(expected_theta)
        expected_y = math.sin(expected_theta)
        
        self.assertAlmostEqual(coord.normal_vector[0], expected_x, places=10)
        self.assertAlmostEqual(coord.normal_vector[1], expected_y, places=10)
    
    def test_antipode_is_opposite(self):
        """Test that antipode is on opposite side of ring"""
        coord = self.geometry.map_number_to_geometry(1981)
        
        # Antipode should be 180 degrees away
        expected_antipode = (181 + 180) % 360
        self.assertEqual(coord.antipode_state, expected_antipode)
    
    def test_multiple_values_round_trip(self):
        """Test round-trip for multiple values"""
        test_values = [0, 1, 100, 360, 1000, 1981, 5000, 10000]
        
        for value in test_values:
            with self.subTest(value=value):
                self.assertTrue(self.geometry.verify_round_trip(value))
    
    def test_cell_index_wraps(self):
        """Test that cell index wraps around ring size"""
        coord1 = self.geometry.map_number_to_geometry(0)
        coord2 = self.geometry.map_number_to_geometry(360)
        coord3 = self.geometry.map_number_to_geometry(720)
        
        # All should map to cell 0
        self.assertEqual(coord1.cell_index, 0)
        self.assertEqual(coord2.cell_index, 0)
        self.assertEqual(coord3.cell_index, 0)
        
        # But have different frequencies
        self.assertNotEqual(coord1.angular_frequency, coord2.angular_frequency)
        self.assertNotEqual(coord2.angular_frequency, coord3.angular_frequency)
    
    def test_get_antipode_coordinate(self):
        """Test getting antipode coordinate"""
        coord = self.geometry.map_number_to_geometry(1981)
        antipode = self.geometry.get_antipode_coordinate(coord)
        
        # Antipode should be at opposite cell
        self.assertEqual(antipode.cell_index, coord.antipode_state)
        
        # Normal vectors should point in opposite directions (approximately)
        dot_product = (coord.normal_vector[0] * antipode.normal_vector[0] + 
                      coord.normal_vector[1] * antipode.normal_vector[1])
        # Dot product should be close to -1 for opposite vectors
        self.assertLess(dot_product, -0.9)
    
    def test_no_randomness(self):
        """Test that there is no randomness in the mapping"""
        results = [self.geometry.map_number_to_geometry(1981) for _ in range(100)]
        
        # All results should be identical
        first = results[0]
        for result in results[1:]:
            self.assertEqual(result, first)
    
    def test_geometric_coordinate_immutable(self):
        """Test that GeometricCoordinate is immutable (NamedTuple)"""
        coord = self.geometry.map_number_to_geometry(1981)
        
        # Should not be able to modify
        with self.assertRaises(AttributeError):
            coord.cell_index = 999
    
    def test_different_ring_sizes(self):
        """Test that different ring sizes work correctly"""
        ring_sizes = [60, 180, 360, 720, 1000]
        
        for size in ring_sizes:
            with self.subTest(ring_size=size):
                geo = Delta1RingGeometry(ring_size=size)
                self.assertTrue(geo.verify_round_trip(1981))
    
    def test_angular_frequency_represents_cycles(self):
        """Test that angular frequency represents number of cycles around ring"""
        coord = self.geometry.map_number_to_geometry(1981)
        
        # 1981 / 360 = ~5.5 complete cycles
        self.assertAlmostEqual(coord.angular_frequency, 5.502777777777778, places=10)
        
        # This means ~5.5 full rotations to reach the position
        cycles = int(coord.angular_frequency)
        self.assertEqual(cycles, 5)


class TestGeometricCoordinate(unittest.TestCase):
    """Test cases for GeometricCoordinate NamedTuple"""
    
    def test_creation(self):
        """Test creating a GeometricCoordinate"""
        coord = GeometricCoordinate(
            cell_index=181,
            normal_vector=(0.5, 0.5),
            angular_frequency=5.5,
            antipode_state=1,
            original_value=1981
        )
        
        self.assertEqual(coord.cell_index, 181)
        self.assertEqual(coord.normal_vector, (0.5, 0.5))
        self.assertEqual(coord.angular_frequency, 5.5)
        self.assertEqual(coord.antipode_state, 1)
        self.assertEqual(coord.original_value, 1981)
    
    def test_tuple_unpacking(self):
        """Test that GeometricCoordinate supports tuple unpacking"""
        coord = GeometricCoordinate(
            cell_index=181,
            normal_vector=(0.5, 0.5),
            angular_frequency=5.5,
            antipode_state=1,
            original_value=1981
        )
        
        cell, normal, freq, antipode, original = coord
        
        self.assertEqual(cell, 181)
        self.assertEqual(normal, (0.5, 0.5))
        self.assertEqual(freq, 5.5)
        self.assertEqual(antipode, 1)
        self.assertEqual(original, 1981)


if __name__ == '__main__':
    unittest.main(verbosity=2)
