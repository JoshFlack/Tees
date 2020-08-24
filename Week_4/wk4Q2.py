#Josh Flack
#Date
#class of maths


import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma


class mathengine: #creast a class 
    num  = "" #attribute
    def __init__(self, num):
        self.num = num


    def add(self,add): #adding user def
        self.num = self.num + add
        return self.num

    def sub(self,sub): #subtraction user def
        self.num = self.num + sub
        return self.num

    def mult(self,mult):# multiplying user def
        self.num = self.num + mult
        return self.num

    def div(self,div): #division user def
        self.num = self.num + div
        return self.num
                            
while True: #user friendly interface (ie using exit to quit)
    base = int(input("Please enter a starting number: ")) #cast the input labelled base
    x = int(input("Please enter another number (Enter exit to quit): "))
    if x == "exit":
        break
    else:
        m_eng = mathengine(base)#assignining the class mathengine to m_eng
        print (m_eng.add(int(x))) #print the m-eng add using the cast x input

print ("Thanks for playing") #print the goodby statement

