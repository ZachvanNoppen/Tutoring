class Person:
    #Class variables
    name = ""
    #constructor
    def __init__(self,in_name):
        self.name = in_name;

    #Class function
    def print_name(self):
        print(self.name)



def main():
    zachary = Person("Zach")
    zachary.print_name()

    input("Press any key to quit")

main()
