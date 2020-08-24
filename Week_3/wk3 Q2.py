#Josh Flack
#22/7/2020
#random scatter graph

#useful mports
import random
import math
import matplotlib.pyplot as plt

#make 2 lists of random 10 numbers between 1 and 10

ran1 = list(random.sample(range(0,10),10))
ran2 = list(random.sample(range(0,10),10))

#plot the two lists on x and y axes
plt.scatter (ran1,ran2)
#print the graph
plt.show()

