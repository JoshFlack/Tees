#Josh Flack - Grades
#15/7/2020

#ask for input of grade from user
grade = (int (input ("Please enter the gradce the student got: ")))

#using if statements work out which grade
#using great than AND less than
if grade < 1:
    print (" No Submision ") #if grade is less than 1 then they did not submit

if grade > 1 and grade < 39: #if grade is greater than 1 AND less than 39
    print ("F") 

if grade > 40 and grade < 49: #if grade is greater than 40 but less than 49
    print ("D")

if grade >50 and grade < 59: #if grade is great than 50 and less than 59
    print ("C")

if grade > 60 and grade < 69: #if grade is greater than 60 and less than 69
    print ("B")
    
if grade > 70 and grade < 79: #if grade is greater than 70 and less than 79
    print ("A")

if grade > 80: #if grade is greater than 80 
    print ("A*")
