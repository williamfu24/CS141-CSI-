# Name: William Fu
# Date: 12/1/2015
# Class: Computer Science 141
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: Program to help the teacher keep track of his students as well as
#   their grades
# Input: User inputs an option from the menu, enabling him to add student
#   and their grades, or quit
# Output: The program changes the list of names and grades, prints these lists
#   looks up a student and their grades, fights the loswest and highest grades
#   and ends the program

def read_gradebook(): #reads in the textfile with the students and their grades
    names=[]          #and seperates the two into seperate lists
    grades=[]
    file = open("gradebook.txt" , "r")
    for line in file:
        line = line.rstrip()
        name, grade= line.split (":")
        grade=int(grade)
        names.append(name)
        grades.append(grade)
    return names, grades

def lookup_grade(names, grades, name): #the function to search the lists of names
    if name in names:                  # for a specific name
        pos=names.index(name)
        return (grades[pos])
    else:
        return -1

def main():
    loop=0 #set up condition of the while loop
    names, grades=read_gradebook()
    while loop!=1: #the menu+options for the program 
        print ("1. Add a new student & grade") 
        print ("2. Print all students") 
        print ("3. Print all grades")
        print ("4. Lookup a student's grade")
        print ("5. Find student with highest grade")
        print ("6. Find student with lowest grade")
        print ("7. Quit")
        options= input("Choose an option:")
        if options=="1":
            new_student=input("What is the new student's name?")
            names.append(new_student)#appends new name unto names list
            new_grade=int(input("What is the new student's grade?"))
            grades.append(new_grade)#appends new grade unto grades list
        elif options=="2":#prints all names
            print ("All students:", names)
        elif options=="3":#prints all grades
            print ("All grades:", grades)
        elif options=="4":#calls the lookup_grade function
            look_up= input("Look up which student?")
            student_grade=lookup_grade(names, grades, look_up)
            if student_grade== -1:
                print("That student doesn't exist")
            else:
                print("Their grade is", student_grade)
        elif options=="5": #finds the highest grade
            ctr=0
            max_pos=0
            for pos in range(0, len(grades)):
                if grades[pos]>ctr:
                    max_pos=pos
                    ctr=grades[pos]
            print("The student with the highest grade is", names[max_pos])
            print("Their grade is", ctr)
        elif options=="6": #finds the lowest grade
            ctr=100
            min_pos=0
            for pos in range (0, len(grades)):
                if grades[pos]<ctr:
                    min_pos=pos
                    ctr=grades[pos]
            print("The student with the lowest grade is", names[min_pos])
            print("Their grade is", ctr)
        elif options=="7": #adds 1 to the loop and ends the while loop
            loop+=1
            print("Done")

