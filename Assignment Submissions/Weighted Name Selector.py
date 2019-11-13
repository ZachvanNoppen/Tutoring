import random


def generate_connections():    
    #           0    1      2         3        4     5       6         7
    family = ['Dad','Mom','Mercy','Sarunas','Zach','Hope','Justus', 'Serena']
    #This is the list that gets changed
    family_available = ['Dad','Mom','Mercy','Sarunas','Zach','Hope','Justus', 'Serena']
    print ("What is your name?")
    my_name = input()
    family_available.remove(my_name)
    family.remove(my_name)
    print ("Who do you want for Christmas?")
    preferred_person = input()
    if preferred_person == "Dont care":
        matched_person = str(random.choices(family_available, k=1))
        print(my_name + ' is matched with '+ matched_person)
        family_available.remove(matched_person)
        
    else:
        #COULD checkc for name in the array
        i = family_available.index(preferred_person)
        if i >=6:
            matched_person = str(random.choices(family_available[i-3:i], weights =[10,10,80], k=1))
        else:
            matched_person = str(random.choices(family_available[i:i+3], weights =[80,10,10], k=1))
        print(my_name + ' is matched with '+ matched_person)
        del family_available[i]

        
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
        if len(family_available) == 0:
            break

    

generate_connections()
#Keeping the window open
input()
