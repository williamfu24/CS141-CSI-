# Name: William Fu
# Project: Potato Heads
# Pledge: I have neither given nor received unauthorized aid on this program. 
# Description: For this program we will be putting eyes, hair, and a mouth onto a
# a Mr Potato head in relation to the x center and the y center of the potato
# Input: The user does not enter commands into the program
# Output: The program is set to draw a Mr. PotatoHead

from simplegraphics import *

# Draw the eyes on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
def draw_eyes(centerx, centery):
    #This part of the program makes the eye
    set_color("white")
    draw_filled_circle(centerx-35, centery-15,25)
    draw_filled_circle(centerx+35, centery-15,25)
    #This part of the program makes the pupil
    set_color("black")
    draw_filled_circle(centerx-35, centery-15,10)
    draw_filled_circle(centerx+35, centery-15,10)
    #This part of the program makes the eyebrow
    draw_filled_rect(centerx-65,centery-55,50,10)
    draw_filled_rect(centerx+15,centery-55,50,10)


# Draw the hair on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
def draw_hair(centerx, centery):
    set_color("black")
    draw_filled_oval(centerx,centery-115,105,40)
    #This part of the program helps make the hat
    draw_filled_oval(centerx,centery-140,75,55)


# Draw the mouth on a potato of radius 150 pixels.
# Parameters: (centerx, centery), the (x, y) coordinates of the potato center.
def draw_mouth(centerx, centery):
    set_color("red")
    draw_filled_polygon(centerx-50,centery+75,centerx-45,centery+100,centerx-5,centery+105,centerx+15,centery+105,centerx+45,centery+100,centerx+50,centery+75)
    set_color("white")
    draw_filled_polygon(centerx-45,centery+80,centerx-40,centery+95,centerx-10,centery+100,centerx+10,centery+100,centerx+40,centery+95,centerx+45,centery+80)
    #This part of the program is a nose
    set_color("red")
    draw_filled_oval(centerx,centery+30,30,25)

# The program starts here.  
# *** DO NOT CHANGE ANY OF THE CODE IN MAIN. ***
def main():
	open_canvas(800, 400)

	# Draw the left potato:
	# Draw a potato-colored circle, centered at (200, 200).
	set_color_rgb(224, 144, 76)
	draw_filled_circle(200, 200, 150)
	set_color("black")

	# Draw the features of the left potato.
	draw_eyes(200, 200)
	draw_hair(200, 200)
	draw_mouth(200, 200)

	# Draw the right potato:
	# Draw a potato-colored circle, centered at (600, 200).
	set_color_rgb(224, 144, 76)
	draw_filled_circle(600, 200, 150)
	set_color("black")

	# Draw the features of the right potato.
	draw_eyes(600, 200)
	draw_hair(600, 200)
	draw_mouth(600, 200)    
	
	close_canvas_after_click()

main()
