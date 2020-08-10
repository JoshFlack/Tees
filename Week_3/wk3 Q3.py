#Josh Flack
#22/7/2020
#Q3 Work Sheet 3

import random as ran
import math as ma
import matplotlib.pyplot as plt

         
def squared(x):
    return x** (n)

n = int (input ("Please enter the power of which you would like to raise the number by"))



l = list (range(0,1001))

sqrd = list(map(squared,l))

plt.scatter (l,sqrd)
plt.show()
