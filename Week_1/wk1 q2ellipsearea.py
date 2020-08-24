#Josh Flack
#24/8/2020
#Ellipse

# ask for radius input for calculation
r1 = input ( "please enter the major axis radius: ")

#asking for the minor axis radius to creat the formula
r2 = input ("please enter minor axis radiius: ")


#making r and interger rather than a string to use for formula
r1 = int (r1)
r2 = int (r2)
pi = 3.141592654

#working out the answer with the forumla below
answer = ((r1 * r2) * pi)

Answer = ("The Area of the ellipse is: ", answer)

#work out the answer by rasing the value of inte r by a power of 2, ie square it
print (Answer)
