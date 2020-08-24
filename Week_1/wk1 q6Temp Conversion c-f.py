#Josh Flack
#24/8/2020
#Temperature Conversion c - f

c = input ("please enter the temperatuyre in celsius: ") #input temp in celcius

c = float(c) #convert to a float

con = 9/5 # making a constant for the equation

far = c*con + 32 # main equation to convert to F

print (c, "Celsius is ", far, "in fahrenheit") #display results
