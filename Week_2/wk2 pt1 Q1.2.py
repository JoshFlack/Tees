#Josh Flack
#18/7/2020
#Cone, sphere and cylinder

import math as m




def cylinder (r,h):
    return (m.pi * ((r**2) * h))



def print_answer_cyl (r,h):
    ans = cylinder (r,h)
    print ("The answer is: ", ans)





    
rad = float (input ("Please enter the radius of the object you have: "))
h = float (input ("Please enter the height: "))
print_answer_cyl (rad,h)








