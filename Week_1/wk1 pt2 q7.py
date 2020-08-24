#Josh Flack
#24/8/2020
# wk1 part 2 q1 and q7

q1 = int(input ("Please enter first number (enter exit to quit)"))
q2 = int(input ("Please enter your second number"))

while q1 != "exit" and q2 != "exit":
   

    if q1 < q2:
        print (q2, ("is bigger than "), q1)

    if q2 < q1:
        print (q1, ("is bigger than "), q2)

    elif q1 == q2:
        print (q1, ("and"), q2, ("are the same"))
    
    break
