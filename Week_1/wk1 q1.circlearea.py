#Josh Flack
#24/8/2020
#circle area program

# ask for radius input for calculation
r = input ( "please enter the radius of the circle ")

#making r and interger rather than a string to use for formula
r = int (r)
pi = 3.141592654 #giving pi the value
answer = (pi *(r**2)) #working out the area of a circle
#answer = ((r * 2) * pi) #working out the circumference answer

Answer = ("The Area is: ", answer)

#work out the answer by rasing the value of inte r by a power of 2, ie square it
print (Answer)
