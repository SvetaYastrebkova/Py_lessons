class Person():
    __counter = 0
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__counter += 1
        self.id = Person.__counter
        pass
    
    def __repr__(self):
        to_print = f"""
        {self.id = }
        {self.name = }
        {self.age = }
        """
        return to_print
    
    def say_word(self, text:str):
        print(f'Person {self.name} talking: {text}')
        pass
    

    
    pass


p1 = Person("Haim", 33)
p2 = Person("Bob", 22)

print(p1) # <__main__.Person object at 0x0000027ACE7A4590> - without __repr implementation
print(p2)

p2.say_word("Hello") # Person Bob talking: Hello