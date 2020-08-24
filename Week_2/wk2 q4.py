#Josh Flack
#20/7/2020
#wk2 Q4 slicing

#useful imports
import math as m
import random as ran
from random import *

#defining the list to be used
rucksack = ["water_flask", \
            "cheese", \
            "gold_coins", \
            "handkerchief", \
            "tinderbox", \
            "scrolls", \
            "dagger", \
            "rope", \
            "nuts", \
            "pipe", \
            "tobacco", \
            "wine_skin", \
            "herbs", \
            "axe",]


rucksack.append ("gems") #append rucksack list to include gems
rucksack.append ("neckless") #append rucksack list to include neckless

rucksack_copy = rucksack [ : ] #create a copy of rucksack list
#print (rucksack_copy)

#use a while loop to count up to 5 random items and then delete those items
c = 0

while c < 5:
    n = ran.randint(0,len(rucksack_copy))
    del rucksack_copy[n]
    c +=1

#print the copied list
print (rucksack_copy)


#rucksack.sort()

 


