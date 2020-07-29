#Josh Flack
#Date
#Name of proram


import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma


class mathengine:
    num  = ""
    def __init__(self, num):
        self.num = num


    def add(self,add):
        self.num = self.num + add
        return self.num

    def sub(self,sub):
        self.num = self.num + sub
        return self.num

    def mult(self,mult):
        self.num = self.num + mult
        return self.num

    def div(self,div):
        self.num = self.num + div
        return self.num
                            
while True:
    base = int(input("Please enter a starting number: "))
    x = input("Please enter another number (Enter exit to quit): ")
    if x == "exit":
        break
    else:
        m_eng = mathengine(base)
        print (m_eng.add(int(x)))

print ("Thanks for playing")

