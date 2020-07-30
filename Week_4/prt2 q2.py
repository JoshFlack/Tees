#Josh Flack
#Date
#Name of proram

import urllib.request as urldl
import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma


def blocked():
    with open("blocked_words.txt", mode="r") as my_file:
         for line in my_file:
             blocked_words = []

while True:

    url = input("Enter address to scan: (enter Exit to quit")
    response = urldl.urlopen(url)
    if url == "Exit":
        break
        

    data = response.read()
    txt = data.decode().lower()

    if blocked_words in txt:
        print ("This bage is blocked ")

    else:
        ("This page is ok to look at")
        

    
