#Josh Flack
#Date
#Name of proram


import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma


class mathengine:
    name = ""
    def __init__(self, num): 
        self.num = num

    def add(self,add):
        self.num = self.num + add
        return self.num

    def sub(self,sub):
        #x = int(input("Please enter a number"))
        ans2 = (x - num)
        return (ans2)

    def mult(self,mult):
        #x = int(input("Please enter a number"))
        ans3 = (x * num)
        return (ans3)

    def div(self,div):
       # x = int(input("Please enter a number"))
        ans4 = (x / num)
        return (ans4)


m_eng = mathengine(45)
m_eng.add(5)
        

#    def greet_to_file(self,filename):
#        with open(filename, 'w') as file: 
#            file.write("hello" + self.name)
        

#greeter = Greeter("Josh")

#greeter.greet_to_file("hi.txt")

#greeter.greet_to_screen()
