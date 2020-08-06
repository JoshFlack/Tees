#Josh Flack
#Date
#Name of proram


import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma


class Greeter:
    name = ""
    def __init__(self, name): # The constructor.
        self.name = name
    def greet_to_screen(self):
        print("Hello,", self.name)

greeter = Greeter("Fred")
greeter.greet_to_screen()
