# Question 7: Implement Polymorphism with Animal classes
# Create a base class Animal and derived classes Dog and Cat
# Each animal should have a speak() method that returns different sounds

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Demonstrate polymorphism
if __name__ == "__main__":
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Dog("Max"),
        Cat("Luna")
    ]
    
    for animal in animals:
        print(animal.speak())
