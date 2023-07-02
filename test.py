class Animal():
    def __init__(self, name):
        self.name = name
        
    def hello(self):
        print(f"Hello, my name is")
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def hello(self):
        print(f"I'm a dog, I bark")
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def hello(self):
        print(f"I'm a cat, I meow")
class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def hello(self):
        print(f"Im a {self.color} cow,I moo.")
        
        
cat = Cat("cat")
dog = Dog("dog")
cow = Cow("Andy", "rainbow")
Animal.hello()
cat.hello()
dog.hello()
cow.hello()