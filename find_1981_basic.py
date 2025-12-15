"""Find the frequency for 1981 BASIC OS and map it to external coordinates"""
from universe import Universe
import math

u = Universe()

# 1981 wraps to cell 504 in the ring
target_year = 1981
cell_1981 = target_year % u.r
print(f"1981 BASIC OS → Cell {cell_1981}")

# Get the normal (direction) at this cell
nx, ny = u.normal(cell_1981, rotated=False)
print(f"Normal vector: ({nx:.6f}, {ny:.6f})")

# Calculate the angle (frequency)
theta = (cell_1981 - 0.5) * u.k
theta_degrees = math.degrees(theta)
print(f"Angle (θ): {theta:.6f} radians = {theta_degrees:.2f}°")

# Map to external coordinates (radius = 100 for visualization)
radius = 100.0
x = radius * nx
y = radius * ny
print(f"\nExternal coordinates (r=100):")
print(f"  x = {x:.2f}")
print(f"  y = {y:.2f}")

# Verify round-trip
cell_check = u.where(x, y)
print(f"\nVerification: where({x:.2f}, {y:.2f}) → Cell {cell_check}")
print(f"Match: {cell_check == cell_1981}")

# Show mirror partner
mirror_1981 = u.mirror(cell_1981)
print(f"\nMirror cell: {mirror_1981}")
mx, my = u.normal(mirror_1981, rotated=False)
print(f"Mirror coordinates: ({radius*mx:.2f}, {radius*my:.2f})")

# Complexity level analysis
print(f"\n{'='*50}")
print(f"1981 BASIC OS PROFILE")
print(f"{'='*50}")
print(f"Cell: {cell_1981}/1477")
print(f"Complexity: {100*cell_1981/u.r:.1f}% of maximum")
print(f"Phase: Early-to-mid complexity")
print(f"Era: Commodore 64, Apple II, TRS-80")
print(f"Features: Line numbers, GOTO, GOSUB, simple arrays")
print(f"Level: Hobbyist/educational programming")
