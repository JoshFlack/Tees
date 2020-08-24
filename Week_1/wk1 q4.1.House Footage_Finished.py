#Josh Flack
#24/8/2020
#Square footage of house


#Data gathering for all rooms
r1w = input ("please enter the width of room 1: ")
r1l = input ("please enter the length of room 1: ")

r2w = input ("Please enter the width for room 2 ")
r2l = input ("Please enter the length for room 2 ")

r3w = input ("Please enter the width for room 3 ")
r3l = input ("Please enter the length for room 3 ")

r4w = input ("Please enter the width for room 4 ")
r4l = input ("Please enter the length for room 4 ")

#Cast all data input to ints

r1w = int(r1w)
r1l = int(r1l)

r2w = int(r2w)
r2l = int(r2l)

r3w = int(r3w)
r3l = int(r3l)

r4w = int(r4w)
r4l = int(r4l)

Area1 = r1w*r1l
Area2 = r2w*r2l
Area3 = r3w*r3l
Area4 = r4w*r4l

#Print the areas for each of the rooms
print ("The areas for the room 1 is: ", Area1)
print ("The areas for the room 2 is: ", Area2)
print ("The areas for the room 3 is: ", Area3)
print ("The areas for the room 4 is: ", Area4)
#print the overal area for the house
print ("The area for the house is: ", Area1+Area2+Area3+Area4) 
