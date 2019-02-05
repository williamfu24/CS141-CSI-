# Name: William Fu
# Project: Bottles
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: This program starts with a high startinng number and removes a certain number of bottles,
# all determined by the user to input. Use of loops help counts the bottles til 0
# Input: The starting number of bottles and the number of bottles removed each time
# Output: Counts the bottles remaining after each removed

def main():
    start_bottle=int(input("How many bottles do we start with?"))
    while start_bottle<=0:
        print("You must start with a positive number of bottles. Please re-enter the number.")
        start_bottle=int(input("How many bottles do we start with?"))
    remove_bottle=int(input("How many bottles do we remove?"))
    while start_bottle<=0:
        print("You must start with a positive number of bottles. Please re-enter the number.")
        start_bottle=int(input("How many bottles do we start with?"))
    bottle_count=start_bottle
    print (bottle_count)
    for bottle_count in range(start_bottle,0,-remove_bottle):
        print(bottle_count, "bottles of pop on the wall,", bottle_count, "bottles of pop.")
        bottle_count=bottle_count-remove_bottle
        if bottle_count<0:
            break
        print("Take", remove_bottle, "down, pass it around", bottle_count, "bottles of pop on the wall.")
main()
