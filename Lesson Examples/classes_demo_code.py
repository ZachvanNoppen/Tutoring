'''
-----------------------
Object Oriented Programming
-----------------------

We've made functions that reduce the amout of code writted, now lets go one step further into program efficiency.

Objects are sections of code that create behaviour unique to sections of memory.

What this means in common vernacular is that we can write code that can create, and recreate (copy) the same object.

An example of OO in real life would be a person. We can have many people and all people have the same characteristics:

Head
Body
Four limbs
Brain
ect...

In code we would write a function that creates these variables and generates values for intelligence, length of limbs, ect... but then we would only ever be able to create one Person
(We could make an array of these values and update the array but extracting and editting that data would be incredibly difficult as seen in the example function below)
Instead we create a class that contains its own variables and functions.

This is called a CLASS

An instance of a CLASS is called an OBJECT

It is important to distinguish the two.

-----------------------
The SELF object
-----------------------
When making classes the default behaviour of python is to ask for object specification
For example, the function print_name below is defined:

def print_name(self):

but when calling it, it is referenced without a parameter:

zachary.print_name()

SELF refers to the current object, so in our case, the 'self' in def print_name(self) refers to the object zachary.


'''
#Polymorphism
'''
ADD CODE HERE

'''

class Person:
    #Class variables
    name = ""
    job = ""
    #constructor
    def __init__(self,in_name, in_job):
        self.name = in_name
        self.job = in_job

    #Class function
    def print_name(self):
        print(self.name)

def main():
    #Function solution

    #Better solution
    '''zachary = Person("Zach", "Student")
    zachary.print_name()'''


    input("Press any key to quit")

main()
