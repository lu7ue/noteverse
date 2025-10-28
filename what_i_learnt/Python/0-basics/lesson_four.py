# Inheritance and Method Overriding Example
class Animal:
    name = ""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats")
    def move(self):
        print("Animal moves")

class Cat(Animal): # Cat inherits from Animal

    def eat(self): # overriding the eat method
        print("Cat eats fish!")
    def meow(self):
        print("Meow!")


# my_cat = Cat("Meowster")
# my_cat.move() # prints "Animal moves"
# my_cat.meow() # prints "Meow!"
# my_cat.eat() # prints "Cat eats fish!" 


# --- This is a horizontal line to separate examples ---

# just a simple class to demonstrate public and private attributes/methods
class Dog:
    name = "" # public attribute: can be accessed from outside the class
    __age = 10 # private attribute: can only be accessed within the class

    def __init__(self, name): # constructor method
        self.name = name
        print(self.__age)

    def eat(self): # public method: can be accessed from outside the class
        print("Dog eats!")
        self.__fight()
    
    def run(self):
        print("Dog runs!")

    def __fight(self): # private method: can only be accessed within the class
        print("Dog fights!")

# my_dog = Dog("Buddy") # create an instance of Dog and prints "10"
# my_dog.eat() # prints "Dog eats!" and "Dog fights!"
# # age = my_dog.__age  # This will raise an AttributeError
# # my_dog.__fight()    # This will also raise an AttributeError
# my_dog.run() # prints "Dog runs!"