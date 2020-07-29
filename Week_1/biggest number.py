first_num = (int (input ("Please enter the first number")))
second_num = (int (input ("Please enter the second number")))
third_num = (int (input ("Please enter the third number")))

if first_num > second_num and first_num > third_num:
    print (first_num)

if second_num > first_num and second_num > third_num:
   print (second_num)

elif third_num > first_num and third_num > second_num:
    print (third_num)
