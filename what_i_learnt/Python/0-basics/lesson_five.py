import lesson_four

# when import a module, the code in the module(lesson_four.py) will be executed
# so the print statements in lesson_four.py will run and show output here
# the solution is hide those print statements in lesson_four.py

cat = lesson_four.Cat("Kitty") # create an instance of Cat class
print(cat.name) # prints "Kitty" - inherited from Animal class
cat.eat() # prints "Cat eats fish!" - overridden method in Cat class
cat.move() # prints "Animal moves" - inherited from Animal class
cat.meow() # prints "Meow!" - defined in Cat class

# --- This is a horizontal line to separate examples ---

from lesson_four import Dog
# use from ... import ... to directly import the Dog class from lesson_four module
# this way we don't need to write lesson_four.Dog every time when using the Dog class

dog = Dog("Buddy") # create an instance of Dog class and prints the private attribute "__age" as "10"
dog.eat() # prints "Dog eats!" and "Dog fights!"
dog.run() # prints "Dog runs!"
