# Volume of a cylinder
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the measurements of a cylindrical
# tank:

radius = 4 # metres
height = 10 # metres

# Also assume that we have imported the existential constant "pi"
# from the "math" library module:

from math import pi

# Write an expression, or expressions, to calculate the volume
# of the tank.  Print the result in a message to the screen.  (If
# you've forgotten the formula for the area of a circle and hence
# volume of a cylinder, ask one of your workshop partners!)

def calc_vol_cylinder():
    '''This is the cylinder fuction
    '''
    print("Enter a radius:")
    input_radius = input()
    print("Enter a height:")
    input_height = input()

    radius=float(input_radius)
    height=float(input_height)

    radius_squared = radius**2

    result = pi * radius_squared * height

    print(f"The volume of the cyliner is: {result} litres")


if __name__ == "__main__":
    calc_vol_cylinder()
