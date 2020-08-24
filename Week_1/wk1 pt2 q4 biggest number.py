#Josh Flack
#24/8/2020
#sorting

first_num = (int (input ("Please enter the first number"))) #ask for first number and cast
second_num = (int (input ("Please enter the second number"))) #ask for second number and cast
third_num = (int (input ("Please enter the third number"))) #ask for third number and cast

if first_num > second_num and first_num > third_num: #if first number is greater than second and third then print first number
    print (first_num)

if second_num > first_num and second_num > third_num: #if second number is greater than first and third number then print second number
   print (second_num)

elif third_num > first_num and third_num > second_num: #else if third number is greater than first and second print third number
    print (third_num)
