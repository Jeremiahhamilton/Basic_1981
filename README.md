# Basic_1981

A deterministic geometric mapping that transforms the number 1981 into a Δ¹ (Delta-1) ring geometry.

## Overview

Instead of treating 1981 as:
- A number you regress on
- A label you tokenize  
- A sequence you slide a window over

This implementation maps 1981 **differently** - folding it into a fixed Δ¹ ring geometry and recovering it as a directional coordinate.

## Features

The geometric mapping provides:
- **Cell Index**: Discrete position on the ring (0-359 for default 360-cell ring)
- **Normal Vector**: Unit vector pointing outward from ring center
- **Angular Frequency**: Number of complete rotations to reach this position
- **Mirror (Antipode) State**: The geometric dual on the opposite side of the ring
- **Reversible Round-Trip**: Perfect reconstruction of the original value

## Key Properties

✅ **No training** - Pure mathematical transformation  
✅ **No simulation** - Direct deterministic computation  
✅ **No learned weights** - Just geometry  
✅ **Fully reversible** - Perfect round-trip recovery

## Usage

### Basic Example

```python
from geometric_mapping import Delta1RingGeometry

# Create the ring geometry
geometry = Delta1RingGeometry(ring_size=360)

# Map 1981 to geometric coordinates
coord = geometry.map_number_to_geometry(1981)

print(f"Cell Index: {coord.cell_index}")           # 181
print(f"Normal Vector: {coord.normal_vector}")     # (-0.999848, -0.017452)
print(f"Angular Frequency: {coord.angular_frequency}")  # 5.502778
print(f"Antipode State: {coord.antipode_state}")   # 1

# Recover the original value
recovered = geometry.recover_from_geometry(coord)
print(f"Recovered: {recovered}")  # 1981
```

### Run the Demonstration

```bash
python3 geometric_mapping.py
```

Output:
```
======================================================================
Geometric Mapping of 1981 to Δ¹ Ring Geometry
======================================================================

Original Value: 1981

Geometric Properties:
  Cell Index:        181
  Normal Vector:     (-0.999848, -0.017452)
  Angular Frequency: 5.502778
  Antipode State:    1

Recovered Value:   1981
Round-trip Valid:  True

Antipode (Mirror) Properties:
  Cell Index:        1
  Normal Vector:     (0.999848, 0.017452)

Verification:
  Deterministic:     True (no randomness)
  No Training:       True (no learned weights)
  Reversible:        True

======================================================================
```

## Mathematical Foundation

### Δ¹ Ring Geometry

The Δ¹ (Delta-1) simplex represents a one-dimensional geometric structure embedded in a circular topology. The ring is divided into discrete cells, with each cell representing a position on the circle.

### Mapping Process

1. **Cell Index Calculation**: `cell_index = value mod ring_size`
   - Maps the value to a discrete position on the ring

2. **Angular Position**: `θ = (2π × cell_index) / ring_size`
   - Converts cell index to radians

3. **Normal Vector**: `(cos(θ), sin(θ))`
   - Unit vector representing directional coordinate

4. **Angular Frequency**: `frequency = value / ring_size`
   - Captures how many complete rotations are needed
   - Preserves information about the "folding"

5. **Antipode State**: `antipode = (cell_index + ring_size/2) mod ring_size`
   - Mirror point on opposite side of ring

### Reversibility

The transformation is reversible because:
- Cell index preserves position within a cycle
- Angular frequency preserves which cycle
- Combined: `value = round(frequency × ring_size)` with cell_index verification

## Testing

Run the comprehensive test suite:

```bash
python3 test_geometric_mapping.py
```

The test suite verifies:
- Correct geometric properties for 1981
- Perfect round-trip recovery
- Deterministic behavior (no randomness)
- Antipode calculations
- Multiple values and ring sizes
- Immutability of coordinates

## Files

- `geometric_mapping.py` - Main implementation
- `test_geometric_mapping.py` - Comprehensive test suite
- `README.md` - This documentation

## License

See LICENSE file for details.
