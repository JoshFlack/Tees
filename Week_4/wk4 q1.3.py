#Josh Flack
#24/8/2020
#Name of proram


import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma

#creat a class
class Greeter:
    name = ""  #the attibute
    def __init__(self, name): # The constructor.
        self.name = name
    def greet_to_screen(self): 
        print("Hello,", self.name)
    def greet_to_file(self): #opening and appending a file
        with open (filename, mode='a') as my_file:
            
        

greeter = Greeter("Fred")
greeter.greet_to_screen()
greeter.greet_to_file("hi.txt")#write the greeting to txt file hi.txt
