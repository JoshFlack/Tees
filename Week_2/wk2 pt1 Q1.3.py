#Josh Flack
#18/7/2020
#Cone, sphere and cylinder

import math as m





def cone (r,h):
    return ((1/3) * m.pi * (r**2) * h)

def print_answer_cone (r,h):
    ans = cone (r,h)
    print(("The answer is: "), ans)
   
r = float (input ("Please enter the radius of the object you have: "))
h = float (input ("Please enter the height: "))

print_answer_cone (r, h)







