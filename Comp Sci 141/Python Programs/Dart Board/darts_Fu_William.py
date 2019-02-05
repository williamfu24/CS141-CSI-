# Name: William Fu
# Project: Darts
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: This programs intention is to take coordinates the user determines
#    and assigns a point value based on where "the dart lands"
# Input:The user inputs the x and y coordinates for the dart thrown
# Output: The program will determine how many points the user will recieve
#    according to the coordinates input

def main():
    x_coor=float(input("What is the x-coordinate where your dart landed?"))
    y_coor=float(input("What is the y-coordinate where your dart landed?"))
    if x_coor>=30 or y_coor>=30 or x_coor<0 or y_coor<0: #eleminates any darts off the board
        print("You win 0 points :(")
    elif x_coor>=20 and y_coor<10 or x_coor<10 and y_coor>=20: #the area for green squares and prints the color and points won
        color="green"
        print("You landed in the", color, "square")
        print("You win 15 points!!!")
    elif x_coor>=0 and y_coor>=10 and y_coor<20: #the area for yellow squares and prints the color and points won
        color="yellow"
        print("You landed in the", color, "square")
        print("You win 10 points!!")
    elif x_coor>=10 and y_coor>=20 or x_coor<20 and y_coor<10:#the area for red squares and prints color square and points won
        color="red"
        print( "You landed in the", color, "square")
        print( "You win 5 points!")

main() #the program is a success

