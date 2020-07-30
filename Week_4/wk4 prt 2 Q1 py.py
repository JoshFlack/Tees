#Josh Flack
#Date
#Name of proram

import urllib.request as urldl
import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma

while True:
    url = input ("Please enter the web address of the file you wish to download")
    dest = input ("Where would you like to save the file? ")
    urldl.urlretrieve (url,dest)
    again = input ("download another file? ")
    if again != "yes":
        break
