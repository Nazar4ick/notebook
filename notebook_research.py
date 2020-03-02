import sys
from main import Note, Notebook
from notebook import Menu


if __name__ == '__main__':
    # creating an object
    # __init__ runs to create an object
    n = Notebook()

    # checking if it is an object
    print(isinstance(n, object))
    # self refers to the object itself
    # we can assign variables to self.variable
    # we can use self.method to run a class method
    n.new_note("Hey, what's up?")
    print(isinstance(n.notes, object))
    print(isinstance(n.notes, list))

    # Methods
    print(dir(Notebook))
    print(dir(Note))
    print(dir(Menu))

    # __str__ method for representing an object
    print(str(n))
