# CLASS INHERITANCE EXPLAINED:
# You can inherit methods and behaviors from an existing class. This is class inheritance.

# class Fish(Animal): # Fish inherists from the animal class
#     def __init__(self):
#         super().__init__() # Fish gets its attributes and methods from the animal class


class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale")
        
class Fish(Animal):
    def __init__(self):
        super().___init__() # These lines (Animal) and super() allow the fish class to inherit methods and attributes from the super class or animal class
    
    def breathe(self): #redefine the breathe function as fishes breathe a bit differently
        super().breathe() # get the current breathe method from Animal super class
        print("doing this under water") #add the difference
    def swim(self):
        print("Moving through water")
        
nemo = Fish()
nemo.swim()
nemo.breathe()
nemo.num_eyes()

#