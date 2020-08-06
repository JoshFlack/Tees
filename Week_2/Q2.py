#Josh Flack
#20/7/2020
#wk2 Q4 slicing

import math as m
import random as ran
from random import *

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


rucksack.append ("gems")
rucksack.append ("neckless")

rucksack_copy = rucksack [ : ]
#print (rucksack_copy)


c = 0

while c < 5:
    n = ran.randint(0,len(rucksack_copy))
    del rucksack_copy[n]
    c +=1

print (rucksack_copy)


#rucksack.sort()

 


