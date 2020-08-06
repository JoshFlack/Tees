#Josh Flack
#20/7/2020
#Dice

import math as m
import random as ran


def die_1_roll():
    return (ran.randint(1,6))


def die_2_roll():
    return (ran.randint(1,6))

lscore = []
def score():
    return (die_1_roll() + die_2_roll())

i = 0
while i<100: #print score 100 times. This is the amount of rolls!
    lscore.append(score())
    print (lscore)  
    i += 1

rec = []

count = 2
t = 0
while t<12:
    x = count
    lscore.count(x)
    rec.append(lscore.count(t))
    count += 1
    t += 1
    print (rec)



#roll =list (range(1,101))
#print (roll)

print (lscore.count(2))
print (lscore.count(3))
print (lscore.count(4))
print (lscore.count(5))
print (lscore.count(6))
print (lscore.count(7))
print (lscore.count(8))
print (lscore.count(9))
print (lscore.count(10))
print (lscore.count(11))
print (lscore.count(12))

#roll.count(1)
#occs_of_1 = roll.count(1)

#print (occs_of_1)
#Display = []


