 #Josh Flack
#18/7/2020
#Cone, sphere and cylinder

import math as m


def sphere(rad):
    return ((4/3) * m.pi * (rad**3))

def cone (rad,h):
    answer = ((1/3) * m.pi * (rad**2) * h)
    return answer 

def cylinder (rad,h):
    return (m.pi * ((rad**2) * h))



rad = float (input ("Please enter the radius of the object you have: "))    
Q = int (input (" Please enter 1 if it is a sphere, 2 if it is a cylinder, or 3 if it is a cone"))  



if  Q == 2:
    h = float (input ("Please enter the height: "))
    cylinder (rad,h)

if Q == 3:
    h = float (input ("Please enter the height: "))
    cone(rad,h)

elif Q == 1:
    print_answer_sphe (rad)






#def print_answer_sphe (r):
#    ans = sphere (r)
  #    print ("The answer is: ", ans)

#def print_answer_cone (r,h):
#    ans = cone (r,h)
#    print ("The answer it: "), ans

#def print_answer_cyl (r,h):
#    ans = cylinder (r,h)
#    print ("The answer is: ", ans)
