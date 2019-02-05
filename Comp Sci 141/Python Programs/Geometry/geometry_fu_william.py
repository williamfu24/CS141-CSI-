# Name: William Fu
# Project: Geometry
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: This program has several steps within it. First it asks for
#   the shape that the user would like to calculate. Then it asks for the
#   variables of the shape and use it to compute the area. Lastly it will
#   print the area. If the shape is not among the list of computable shapes
#   the program will print an error message
# Input: The user enters a shape they want to calculate and the variables
#   for the shape
# Output: The program takes the shape and determines which program/formula
#   to run and takes the variables the user entered to find the area

def main():
    loop="yes"
    while loop == "yes" or loop=="Yes":
        shape=input("What shape would you like to calculate?")
        if shape== "circle" or shape=="Circle":
            area=circle()
            print("The area of the circle is", area)
        elif shape=="rectangle" or shape=="Rectangle":
            area=rectangle()
            print("The area of the rectangle is", area)
        elif shape=="square" or shape=="Square":
            area=square()
            print("The area of the square is", area)
        elif shape=="prism" or shape == "Prism":
            surface_area=prism()
            print("The surface area of the prism is", surface_area)
        elif shape ==  "ring" or shape == "Ring":
            area=ring()
            print("The area of the ring is", area)
        else:
            print("I dont know that shape")
        loop=input("Do you want to calculate another one?")

def circle():
    radius=int(input("What is the radius of the circle?"))
    return 3.14*(radius**2)
    
def rectangle():
    length=int(input("What is the length of the rectangle?"))
    width=int(input("What is the width of the rectangle?"))
    return length*width

def square():
    side=int(input("What is the side length of the square?"))
    return side**2

def prism():
    length=int(input("What is the length of the prism?"))
    width=int(input("What is the width of the prism?"))
    height=int(input("What is the height of the prism?"))
    x=(length*width)
    y=(height*length)
    z=(height*width)
    return 2*(x+y+z)

def ring():
    radius_1=int(input("What is the outer radius?"))
    radius_2=int(input("What is the inner radius?"))
    circle_1=3.14*(radius_1**2)
    circle_2=3.14*(radius_2**2)
    return circle_1-circle_2

main()
