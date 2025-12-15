"""
Geometric Mapping of 1981 to Δ¹ Ring Geometry

This module implements a deterministic geometric transformation that maps
the number 1981 into a fixed Δ¹ (Delta-1) ring geometry, recovering it as
a directional coordinate with:
- Cell index
- Normal vector
- Angular frequency
- Mirror (antipode) state
- Reversible round-trip back to origin

No training, no simulation, no learned weights - just deterministic geometry.
"""

import math
from typing import Tuple, NamedTuple


class GeometricCoordinate(NamedTuple):
    """Represents a point in Δ¹ ring geometry"""
    cell_index: int
    normal_vector: Tuple[float, float]
    angular_frequency: float
    antipode_state: int
    original_value: int


class Delta1RingGeometry:
    """
    Δ¹ Ring Geometry - A one-dimensional simplex embedded in a circular topology.
    
    The ring is divided into discrete cells, each representing a position on the
    circle. The geometry preserves directional information and allows for reversible
    transformations.
    """
    
    def __init__(self, ring_size: int = 360):
        """
        Initialize the Δ¹ ring geometry.
        
        Args:
            ring_size: Number of discrete cells in the ring (default: 360 for degree-like representation)
        """
        self.ring_size = ring_size
        self.modulus = ring_size
    
    def map_number_to_geometry(self, value: int) -> GeometricCoordinate:
        """
        Map a number to its geometric representation in the Δ¹ ring.
        
        This uses a deterministic folding operation to embed the number into
        the ring geometry, computing all geometric properties.
        
        Args:
            value: The integer value to map (e.g., 1981)
        
        Returns:
            GeometricCoordinate containing all geometric properties
        """
        # 1. Cell Index: Map value to a discrete position on the ring
        cell_index = value % self.ring_size
        
        # 2. Angular position in radians [0, 2π)
        theta = (2 * math.pi * cell_index) / self.ring_size
        
        # 3. Normal Vector: Unit vector pointing outward from ring center
        # This represents the directional coordinate
        normal_x = math.cos(theta)
        normal_y = math.sin(theta)
        normal_vector = (normal_x, normal_y)
        
        # 4. Angular Frequency: How many complete rotations to reach this position
        # This captures the "folding" information
        angular_frequency = value / self.ring_size
        
        # 5. Antipode State: The mirror point on the opposite side of the ring
        # This is the geometric dual of the current position
        antipode_cell = (cell_index + self.ring_size // 2) % self.ring_size
        antipode_state = antipode_cell
        
        return GeometricCoordinate(
            cell_index=cell_index,
            normal_vector=normal_vector,
            angular_frequency=angular_frequency,
            antipode_state=antipode_state,
            original_value=value
        )
    
    def recover_from_geometry(self, coord: GeometricCoordinate) -> int:
        """
        Recover the original number from its geometric representation.
        
        This implements the reversible round-trip transformation.
        
        Args:
            coord: GeometricCoordinate to recover from
        
        Returns:
            The original integer value
        """
        # Reconstruct from cell_index and angular_frequency
        # Since we know: value = (angular_frequency * ring_size) rounded to nearest cell
        recovered = int(round(coord.angular_frequency * self.ring_size))
        
        # Verify the cell_index matches
        if recovered % self.ring_size != coord.cell_index:
            # Adjust to ensure cell_index consistency
            cycles = recovered // self.ring_size
            recovered = cycles * self.ring_size + coord.cell_index
        
        return recovered
    
    def verify_round_trip(self, value: int) -> bool:
        """
        Verify that the round-trip transformation is reversible.
        
        Args:
            value: The value to test
        
        Returns:
            True if value -> geometry -> value is perfect
        """
        coord = self.map_number_to_geometry(value)
        recovered = self.recover_from_geometry(coord)
        return recovered == value
    
    def get_antipode_coordinate(self, coord: GeometricCoordinate) -> GeometricCoordinate:
        """
        Get the mirror/antipode coordinate on the opposite side of the ring.
        
        Args:
            coord: The original coordinate
        
        Returns:
            The antipode coordinate
        """
        # Calculate antipode value by maintaining frequency but flipping position
        antipode_value = int(coord.angular_frequency * self.ring_size)
        antipode_value = (antipode_value + self.ring_size // 2)
        
        return self.map_number_to_geometry(antipode_value)


def demonstrate_1981_mapping():
    """
    Demonstrate the geometric mapping of 1981.
    
    This shows how 1981 is folded into the Δ¹ ring geometry and recovered.
    """
    print("=" * 70)
    print("Geometric Mapping of 1981 to Δ¹ Ring Geometry")
    print("=" * 70)
    print()
    
    # Create the ring geometry
    geometry = Delta1RingGeometry(ring_size=360)
    
    # Map 1981 to geometry
    value = 1981
    coord = geometry.map_number_to_geometry(value)
    
    print(f"Original Value: {value}")
    print()
    print("Geometric Properties:")
    print(f"  Cell Index:        {coord.cell_index}")
    print(f"  Normal Vector:     ({coord.normal_vector[0]:.6f}, {coord.normal_vector[1]:.6f})")
    print(f"  Angular Frequency: {coord.angular_frequency:.6f}")
    print(f"  Antipode State:    {coord.antipode_state}")
    print()
    
    # Demonstrate reversibility
    recovered = geometry.recover_from_geometry(coord)
    print(f"Recovered Value:   {recovered}")
    print(f"Round-trip Valid:  {recovered == value}")
    print()
    
    # Show antipode
    antipode_coord = geometry.get_antipode_coordinate(coord)
    print("Antipode (Mirror) Properties:")
    print(f"  Cell Index:        {antipode_coord.cell_index}")
    print(f"  Normal Vector:     ({antipode_coord.normal_vector[0]:.6f}, {antipode_coord.normal_vector[1]:.6f})")
    print()
    
    # Verify the geometry
    print("Verification:")
    is_valid = geometry.verify_round_trip(value)
    print(f"  Deterministic:     True (no randomness)")
    print(f"  No Training:       True (no learned weights)")
    print(f"  Reversible:        {is_valid}")
    print()
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_1981_mapping()
