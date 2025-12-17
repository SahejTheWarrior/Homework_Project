import math

try:
    angle = float(input("Enter angle in degrees: "))

    radians = math.radians(angle)

    print("Sine value:", math.sin(radians))
    print("Cosine value:", math.cos(radians))
    print("Tangent value:", math.tan(radians))

except ValueError:
    print("Invalid input! Please enter a numeric value.")
