# Name: William Fu
# Project: Connect The Dots
# Pledge: I have neither given nor received unauthorized aid on this program. 
# Description: This program asks a user for a file, drawing a picture using
#   code from the file the user called, and then closing after a click on canvas
# Input: User is asked for a file and inputs one of the five
# Output: This program takes the file, reads the lines and turns the lines
#   into coordinates for a drawing

from simplegraphics import *

def main():
    #ask for what file needs reading
    file_name=input("Which file would you like to open?") #asks for file to use
    if file_name != "shapes.txt" and file_name != "two-triangles.txt"\
       and file_name != "stars.txt" and file_name != "panda.txt"\
       and file_name !="homer.txt": #if file doesnt match then it asks for a new one
        print("That is not a valid file. Please pick another")
        main()
    convert(file_name)#calls the conver program
    close_canvas_after_click() #closes canvas after click


def convert(file_name): #takes file and converts to make easier to use in progrm
    open_canvas(400,400) #opens canvas
    x1=0
    y1=0
    ctr=0
    file = open(file_name, "r") #opens file, reads it
    for line in file:
        line=line.rstrip()
        x,y=line.split(" ") #seperates variables, and turns into integers
        x2=int(x)
        y2=int(y)

        if ctr>0:
            if x1!=-1 or y1!=-1:#ensures program wont use as a starting coordinate
                if x2!=-1 or y2!=-1:#ensures program wont use as a ending coordinate
                    draw(x1,y1,x2,y2)#calls the draw program
        x1=x2  #uses sliding windows to keep track of previous

        y1=y2  #coordinates so draw works
        ctr+=1 #uses counter to skip the first line drawing
                #where there would only be 1 set or coordinates


def draw(x1,y1,x2,y2):
    draw_line(x1,y1,x2,y2)
