# Python Program for Calculating the Area of a Circle

import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Input: Get the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Call the function and print the result
circle_area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")
