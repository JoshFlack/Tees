#Josh Flack
#Date: 8/7/2020
#Eligible Voters

#requestin input from user
name = input ("please enter your name: ")
age = (int (input("please enter your age: ")))
cont = input ("please enter your country or citizenship: ")
Allowed = "Britain"

#nest condition to estabilish if they can vote.
if age > 18 and cont == Allowed:
     print (name, "you are allowed to vote")

else:
    print (name, "you are not allowed to vote")
