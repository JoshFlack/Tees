#Josh Flack
#24/8/2020
#Grading list 


data = [ "Fozzie", 34, \
         "Kermit", 78, \
         "Miss Piggy", 23, \
         "Gonzo", 55, \
         "Beaker", 88, \
         "Honeydew", 59, \
         "Animal", 10, \
         "Rowlf", 54, \
         "Bunsen", 70, \
         "Walter", 51, \
         "Sam Eagle", 19, \
         "Scooter", 62, \
         "Pepe", 45, \
         "Gremlin", 4, \
         "Sweetums", 60, \
         "Hoggart", 39, \
         "Skittle", 49, \
         "Gumbal", 38, \
         "Rizzo", 45, \
         "Bratrat", 14,
         "Mongo", 95]


clean_data = [] #make clean/easy to use data list

i = 0 #counter to move onto the next indicie

while i < len(data):
    person = {
        "name": data[i],
        "grade": data [i+1]
    }
    print (person["name"])
    print (person ["grade"])
    i +=2 #add 2 to the counter to move onto the next persons info
    clean_data.append(person)

#grad marks

fal = 39
pas = 40
mer = 60
dis = 70

Fail = list(filter(lambda x: x["grade"] < pas, clean_data)) #filter list for people who failed or did not hand in
print ("These people failed", Fail) #print the filtered list

Pass = list(filter(lambda x: x["grade"] > pas and x["grade"] < mer, clean_data)) #filter list for pass grades
print ("These people graded a pass", Pass) #print the filter list

Merit = list(filter(lambda x: x["grade"] > mer and x["grade"] < dis, clean_data)) #filters list for merit grades
print ("These people graded a Merit grade", Merit) #print the filtered list

Distinction = list(filter(lambda x: x["grade"] > dis, clean_data)) #filter the list for distinction grades
print ("These people graded a Distinction grade", Distinction) #print the filtered list


print ("This person had the top grade", (max(clean_data, key=lambda x: x["grade"]))) #This filters through and gives the highest grade




  
