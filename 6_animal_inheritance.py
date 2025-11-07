# Inheritance demonstration with Animal base class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def fetch(self):
        print(f"{self.name} is fetching the ball!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def meow(self):
        print(f"{self.name} says: Meow!")
    
    def scratch(self):
        print(f"{self.name} is scratching the furniture.")

# Example usage
dog = Dog("Buddy", "Golden Retriever")
print(f"Dog: {dog.name} ({dog.breed})")
dog.eat()
dog.bark()
dog.fetch()

print()
cat = Cat("Whiskers", "Orange")
print(f"Cat: {cat.name} ({cat.color})")
cat.eat()
cat.meow()
cat.scratch()
