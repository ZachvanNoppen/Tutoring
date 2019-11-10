import random

# We have a hat
# We draw a name (random) from the family
# IF the name is not ours, then it's good
# Remove the name from the hat
def generate_connections():
    #           0    1      2         3        4     5       6         7
    family = ['Dad','Mom','Mercy','Sarunas','Zach','Hope','Justo', 'Serena']
    #This is the list that gets changed
    family_available = ['Dad','Mom','Mercy','Sarunas','Zach','Hope','Justo', 'Serena']
    #matching every person
    for person in range(len(family)):
        #Generating a random person that is still in the list
        random_person = random.randint(0,len(family_available)-1)
        #Making sure it's not itself
        while(random_person == person):
            random_person = random.randint(0,len(family_available)-1)

        #Printing the result (this will only happen when the loop above breaks)
        print(family[person] + ' is matched with '+ family_available[random_person])
        #removing the person picked from the list
        del family_available[random_person]


generate_connections()
#Keeping the window open
input()
