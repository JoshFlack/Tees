
#Data gathering for all rooms
r1w = input ("please enter the width of room 1: ")
r1l = input ("please enter the length of room 1: ")
r1h = input ("Please enter the hieght of room 1: ")

r2w = input ("Please enter the width for room 2 ")
r2l = input ("Please enter the length for room 2 ")
r2h = input ("Please enter the hieght of room 2: ")

r3w = input ("Please enter the width for room 3 ")
r3l = input ("Please enter the length for room 3 ")
r3h = input ("Please enter the hieght of room 3: ")

r4w = input ("Please enter the width for room 4 ")
r4l = input ("Please enter the length for room 4 ")
r4h = input ("Please enter the hieght of room 4: ")

#Cast all data input to ints

r1w = int(r1w)
r1l = int(r1l)
r1h = int(r1h)

r2w = int(r2w)
r2l = int(r2l)
r2h = int(r2h)

r3w = int(r3w)
r3l = int(r3l)
r3h = int(r3h)

r4w = int(r4w)
r4l = int(r4l)
r4h = int(r4h)

Area1 = r1w*r1l
Area2 = r2w*r2l
Area3 = r3w*r3l
Area4 = r4w*r4l

Volume1 = Area1*r1h
Volume2 = Area2*r2h
Volume3 = Area3*r3h
Volume4 = Area4*r4h

#print ("The area for the room 1 is: ", Area1)
#print ("The areas for the room 2 is: ", Area2)
#print ("The areas for the room 3 is: ", Area3)
#print ("The areas for the room 4 is: ", Area4)

print ("Volume for room 1 is: ", Volume1)
print ("Volume for room 2 is: ", Volume2)
print ("Volume for room 3 is: ", Volume3)
print ("Volume for room 4 is: ", Volume4)


#print ("The area for the house is: ", Area1+Area2+Area3+Area4) 
print ("Volume for the house is: ", Volume1+Volume2+Volume3+Volume4)
