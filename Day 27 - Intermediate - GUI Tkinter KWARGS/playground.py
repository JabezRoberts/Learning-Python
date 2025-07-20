# UNLIMITED POSITIONAL ARGUMENTS
# /*args is a tuple
# Modify the add function to take an unlimited number of arguments and add them all using a for loop
def add(*args): # args is entered as a tuple
    sum = 0
    for n in args:
        sum += n
    print(sum) # return sum then enter print(add(3,5,6))

add(3,5,6)


# UNLIMITED NUMBER OF Keyword Arguments
# /**kwargs is a dictionary
def calculate(**kwargs):
    print(kwargs) # print dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])

calculate(add=3, multiply=5)


def calculate1(n,**kwargs):
    print(kwargs) # print dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
                

calculate1(2, add=3, multiply=5) # Gives us n + 3 which is 5 then this n = 5 multiply 5 which is 25



class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
my_car = Car(make="Nissan")
print(my_car.model)
# printing my_car.make would return Nissan but my_car.model would return an error if we used self.model = kw["model"] to access the value via the dictionary key. 
# By using the .get() method the function returns None if there is no model specified in the function call like above