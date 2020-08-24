#Josh Flack
#20/7/2020
#wk2 Q4 slicing

import math as m
import random as ran
from random import *

#make a list of current contentce of sack
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

#append the rucksack to include these
rucksack.append ("gems")
rucksack.append ("neckless")

#sort the rucksack list into accending order
rucksack.sort()

rucksack_copy = rucksack [ : ]
#print (rucksack_copy)

#select 5 random items for rucksack list using a while loop
c = 0

while c < 5:
    n = ran.randint(0,len(rucksack_copy))
    del rucksack_copy[n]
    c +=1

#print the rucksack copy list
print (rucksack_copy)




 


