#Josh Flack
#24/8/2020
#download url

#useful imports
import urllib.request as urldl
import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma

while True: #use a while true loop incase user wants to exit
    url = input ("Please enter the web address of the file you wish to download") #ask users for url address to download
    dest = input ("Where would you like to save the file? ") #ask user where to download url to on computer
    urldl.urlretrieve (url,dest) #the action of downloading the url and the destination of where to download it to
    again = input ("download another file? ") #ask the user if they want to downlaod another file
    if again != "yes":
        break
