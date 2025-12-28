
# create class

class Person :
    # data
    class_description = "My Person class"
    name:str = "NO_NAME"    
    
    # methods
    ## Class constructor
    def __init__(self,name, age):
        self.name = name
        
        pass
    
    def tell_something(self):
        print("I am object of " + self.class_description)        
        
        pass
    
   
    pass


# Create object

person1 = Person("Haim") # call class constructor
person2 = Person("Bob")

person1.tell_something()
person2.tell_something()

print(person1.class_description)
print(person2.class_description)
print(Person.class_description)

print(person2.name)
print(person1.name)  # getting self.name
print(Person.name)  # 