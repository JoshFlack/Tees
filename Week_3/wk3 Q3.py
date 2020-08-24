#Josh Flack
#22/7/2020
#Q3 Work Sheet 3

#useful imports
import random as ran
import math as ma
import matplotlib.pyplot as plt

#user defined definition         
def squared(x):
    return x** (n)

#ask for an input
n = int (input ("Please enter the power of which you would like to raise the number by"))


#create a list l using numbers between 1 and 1000
l = list (range(0,1001))

#create another list called sqrd using def squared where n = 1
sqrd = list(map(squared,l))

#creat a scatter graph using l and sqrd on x and y axes
plt.scatter (l,sqrd)
#print the graph
plt.show()
