# Student marks data file (do not modify!)
# Pete Dwyer 01/11/17
# Saul Johnson 28/04/2020

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
    i +=2 #add 2  to the counter to move onto the next persons info

fal = 39
pas = 40
mer = 60
dis = 70

Fail = clean_data = list(filter(lambda x: x["grade"] < pas, clean_data))
print ("These people failed", Fail)

Pass = list(filter(lambda x: x["grade"] > pas and x["grade"] < mer, clean_data))
print ("These people graded a pass", Pass)

Merit = list(filter(lambda x: x["grade"] > merit and x["grade"] < dis, clean_data))
print ("These people graded a Merit grade", Merit)

Distinction = list(filter(lambda x: x["grade"] > dis, clean_data))
print ("These people graded a Distinction grade", Distinction)





print (clean_data)


  
