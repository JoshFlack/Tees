#Josh Flack
#20/7/2020
#Dice

#useful imports
import math as m
import random as ran


def die_1_roll():
    return (ran.randint(1,6)) # create random numbers 1 to 6 and put in this def


def die_2_roll():
    return (ran.randint(1,6)) # creat random numbers 1 to 6 and put in this def

lscore = [] # the score of die 1 and die2  added together
def score():
    return (die_1_roll() + die_2_roll())

i = 0
while i<100: #print score 100 times. This is the amount of rolls!
    lscore.append(score())
    #print (lscore)  
    i += 1
#create a new list call rec 
rec = []

#use a while loop to roll 12 times
count = 2
t = 0
while t<12:
    x = count #counter for the while loop
    lscore.count(x)
    rec.append(lscore.count(t)) #append the rec list using the score count (t)
    count += 1 #increase the count by 1
    t += 1
    print (rec)



#print the amount of each number, with the correct amount of *'s next to each number
print ("1",(lscore.count(1)), ("*" *(lscore.count(1))))
print ("2",(lscore.count(3)), ("*" *(lscore.count(3))))
print ("3",(lscore.count(4)), ("*" *(lscore.count(4))))
print ("4",(lscore.count(5)), ("*" *(lscore.count(5))))
print ("5",(lscore.count(6)), ("*" *(lscore.count(6))))
print ("6",(lscore.count(7)), ("*" *(lscore.count(7))))
print ("7",(lscore.count(8)), ("*" *(lscore.count(8))))
print ("8",(lscore.count(9)), ("*" *(lscore.count(9))))
print ("9",(lscore.count(10)), ("*" *(lscore.count(10))))
print ("10",(lscore.count(11)), ("*" *(lscore.count(11))))
print ("11",(lscore.count(12)), ("*" *(lscore.count(12))))
print ("12",(lscore.count(12)), ("*" *(lscore.count(12))))




