"""
Visualization helper for Δ¹ ring geometry.

This module provides text-based visualization of how numbers are mapped
to the ring geometry, showing the angular positions and relationships.
"""

from geometric_mapping import Delta1RingGeometry
import math


def visualize_ring_position(value: int, ring_size: int = 360):
    """
    Create a text-based visualization of a value's position on the ring.
    
    Args:
        value: The number to visualize
        ring_size: Size of the ring
    """
    geometry = Delta1RingGeometry(ring_size=ring_size)
    coord = geometry.map_number_to_geometry(value)
    
    print(f"\nVisualization of {value} on Δ¹ Ring (size={ring_size})")
    print("=" * 60)
    
    # Create a simple compass-like display
    theta = (2 * math.pi * coord.cell_index) / ring_size
    degrees = (theta * 180 / math.pi) % 360
    
    # Determine quadrant and direction
    if degrees < 45 or degrees >= 315:
        direction = "East (→)"
    elif degrees < 135:
        direction = "North (↑)"
    elif degrees < 225:
        direction = "West (←)"
    else:
        direction = "South (↓)"
    
    print(f"Position: Cell {coord.cell_index} of {ring_size}")
    print(f"Angle: {degrees:.1f}° from East")
    print(f"Direction: {direction}")
    print(f"Rotations: {coord.angular_frequency:.2f} complete cycles")
    print()
    
    # ASCII art ring representation
    print("Ring Position (approximate):")
    print()
    
    # Create a simple 8-point compass visualization
    positions = [
        (0, "  0° →"),
        (45, " 45° ↗"),
        (90, " 90° ↑"),
        (135, "135° ↖"),
        (180, "180° ←"),
        (225, "225° ↙"),
        (270, "270° ↓"),
        (315, "315° ↘")
    ]
    
    for pos_deg, label in positions:
        if abs(degrees - pos_deg) < 22.5 or (pos_deg == 0 and degrees > 337.5):
            print(f"    {label}  ← VALUE IS HERE")
        else:
            print(f"    {label}")
    
    print()
    
    # Show antipode
    antipode_coord = geometry.get_antipode_coordinate(coord)
    antipode_degrees = ((2 * math.pi * antipode_coord.cell_index) / ring_size * 180 / math.pi) % 360
    
    print(f"Antipode (mirror) at cell {antipode_coord.cell_index}")
    print(f"Antipode angle: {antipode_degrees:.1f}°")
    print(f"Distance: 180° apart (opposite side of ring)")
    print()
    
    # Show vector representation
    print("Normal Vector Components:")
    print(f"  X: {coord.normal_vector[0]:+.6f}")
    print(f"  Y: {coord.normal_vector[1]:+.6f}")
    print(f"  Magnitude: {math.sqrt(coord.normal_vector[0]**2 + coord.normal_vector[1]**2):.6f}")
    print()
    
    # Verify round trip
    recovered = geometry.recover_from_geometry(coord)
    print(f"Round-trip test: {value} → geometry → {recovered}")
    print(f"Success: {recovered == value}")
    print("=" * 60)


def compare_values(values: list, ring_size: int = 360):
    """
    Compare multiple values and their positions on the ring.
    
    Args:
        values: List of values to compare
        ring_size: Size of the ring
    """
    geometry = Delta1RingGeometry(ring_size=ring_size)
    
    print(f"\nComparison of Values on Δ¹ Ring (size={ring_size})")
    print("=" * 80)
    print(f"{'Value':<10} {'Cell':<6} {'Angle (°)':<12} {'Frequency':<12} {'Antipode':<10}")
    print("-" * 80)
    
    for value in values:
        coord = geometry.map_number_to_geometry(value)
        theta = (2 * math.pi * coord.cell_index) / ring_size
        degrees = (theta * 180 / math.pi) % 360
        
        print(f"{value:<10} {coord.cell_index:<6} {degrees:<12.2f} "
              f"{coord.angular_frequency:<12.4f} {coord.antipode_state:<10}")
    
    print("=" * 80)


def demonstrate_folding(base_value: int = 181, ring_size: int = 360):
    """
    Demonstrate how values fold onto the same cell with different frequencies.
    
    Args:
        base_value: The base cell position
        ring_size: Size of the ring
    """
    geometry = Delta1RingGeometry(ring_size=ring_size)
    
    print(f"\nFolding Demonstration: Values mapping to Cell {base_value}")
    print("=" * 70)
    
    # Generate values that map to the same cell
    values = [base_value + i * ring_size for i in range(6)]
    
    print(f"All these values map to cell {base_value} but with different frequencies:")
    print()
    
    for value in values:
        coord = geometry.map_number_to_geometry(value)
        print(f"  Value {value:5d} → Cell {coord.cell_index:3d}, "
              f"Frequency: {coord.angular_frequency:.4f} "
              f"(≈{int(coord.angular_frequency)} rotations)")
    
    print()
    print("Notice: Same cell position, but frequency increases linearly!")
    print("This is how the ring 'folds' larger numbers into the same geometry.")
    print("=" * 70)


if __name__ == "__main__":
    # Visualize 1981
    visualize_ring_position(1981)
    
    # Compare several values
    print("\n")
    compare_values([0, 90, 180, 360, 1000, 1981, 5000])
    
    # Demonstrate folding
    print("\n")
    demonstrate_folding(181)
