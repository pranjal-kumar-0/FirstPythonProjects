class Mammal:
    def walk(self):
        print('Walk!')


class Dog(Mammal):  #copies the functions in mammal
    pass            #we can add fns individual to dog class or just no change by writing pass.


class Cat(Mammal):
    pass


dog = Dog()
dog.walk()

