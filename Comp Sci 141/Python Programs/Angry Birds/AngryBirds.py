# Name: William Fu
# Project: Angry Birds
# Pledge: I have neither given nor received unauthorized aid on this program. 
# Description: Angry Birds where user inputs a file to read the level set up and
# program keeps track of health and pigs alive
# Input: Bird types and File/level selection
# Output: The game: draws the pigs with their health. launches birds dealing specific
#damage to specific targets

from simplegraphics import *


def read_pigs(): #program to ask for the file name and then read in the pig types converting it to pig energies
    filename= input("What is the file name?")  
    file = open(filename, "r")
    pig_energies = []
    for line in file:
        line = line.rstrip()
        if line == "regular":
            pig_energy=1
        elif line =="helmet":
            pig_energy=2
        elif line == "moustache":
            pig_energy=3
        elif line == "king":
            pig_energy=5
        pig_energies.append(pig_energy) #adds converted pig->energies to a list
    return pig_energies
    file.close()
 
def all_defeated(pig_energies): #program to check if all pigs have been defeated or not
    pigs_alive = 0
    for pos in range(0, len(pig_energies)):
        if pig_energies[pos] > 0:
            pigs_alive += 1
     
    if pigs_alive > 0:
        return False
    else:
        return True
     
 
def launch_red_bird(position,pig_energies): #attacks a specific pig
    pig_energies[position] -= 1


def launch_blue_bird(pig_energies): #attacks all pigs
    for pos in range (0, len(pig_energies)):
        pig_energies[pos] -=1

def launch_purple_bird(pig_energies): #attacks the strongest pig
    ctr=0
    position=0
    for pos in range (0, len(pig_energies)):
        if pig_energies[pos]>ctr:
            ctr=pig_energies[pos]
            position=pos
    pig_energies[position]-=1

def launch_orange_bird(pig_energies): #attacks the weakest living pig
    ctr=1000
    position=0
    for pos in range (0, len(pig_energies)):
        if pig_energies[pos]<ctr and pig_energies[pos]>0:
            ctr=pig_energies[pos]
            position=pos
    pig_energies[position]-=1

def draw_pigs(pig_energies): #program to draw the pigs
    draw_line(0,80,500,80)
    for pos in range (0, len(pig_energies)): #reads in the pigs and their energy from the pig_energies list
        if pig_energies[pos]<=0: #dead pigs are not drawn
            pass
        elif pig_energies[pos] >0:#draws live pigs with energy levels
            draw_circle((((500/(len(pig_energies)+1))*(pos+1))), 50, 30)
            draw_string(str(pig_energies[pos]), (((500/(len(pig_energies)+1))*(pos+1))),50, 10)
        


def main(): #main program bringing everything together
    open_canvas(500,100) #opens canvas enabling draw_pigs() to work
    pig_energies=read_pigs()
    all_defeated(pig_energies)
    while all_defeated(pig_energies) == False: #loop keeping the game running if pigs are still alive
        print(pig_energies)
        draw_pigs(pig_energies)
        choice=input("What kind of bird would you like to launch?") #choice of bird attack
        if choice == "Red" or choice =="red": 
            position=int(input("What position would you like to attack?"))
            launch_red_bird(position,pig_energies)
        elif choice == "Blue" or choice =="blue":
            launch_blue_bird(pig_energies)
        elif choice == "Purple" or choice =="purple":
            launch_purple_bird(pig_energies)
        elif choice == "Orange" or choice =="orange":
            launch_orange_bird(pig_energies)
        else:
            print("Please pick a correct color") #ensures bird is actually avaliable/chosen
        all_defeated(pig_energies)
        clear_canvas() #resets canvas
    close_canvas()
    print("Game Over")
