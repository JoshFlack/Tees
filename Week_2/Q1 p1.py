#Josh Flack
#19/7/2020
#Q 1 part 1

import math as m


#def sphere(r):
    #return (4/3 * m.pi * (r**3))

#def cone (r,h):
 #   return ((1/3) * m.pi * (r**2) * h)

#def cylinder (r,h):
 #   return (m.pi * ((r**2) * h))


def print_answer (r,h):
    ans = sphere (r,h)
    print ("The answer is ", ans)

rad =  float (input ("please enter a radius: "))
h = float (input ("Please enter the hieght: "))
print_answer (rad, h)
