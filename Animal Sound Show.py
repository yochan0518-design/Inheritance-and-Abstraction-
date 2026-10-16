from abc import ABC, abstractmethod


#---ABSTRACT BASE CLASS ( PARENT )---------
#animal inherits from ABC - this makes it an abtract class (abstraction)
class animal (ABC):

    #parent constructor - stores attribuites shared by all the animals 
    def _init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def displayed(self):
        print(f"Name: (self.name) | Haitat: (self.habitat)")

    @abstractmethod
    def speak(self):
        pass

class Dog(animal):

    def __int__(self, name, habitat, breed):
        super().__init__(name, habitat) 
        self.breed = breed

    def speak(self):
        print(f"(self.name) ((self.breed)) says: Woof Woof!")

class Parrot(animal):

    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    def speak(self):
            print(f"(self.name) says: {self.phrase}! {self.pharse}!")

    
class Lion(animal):

    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
            print(f"{self.name} (Pride: {self.pride}) says: ROARRR!")

dog  =Dog("Bruno", "Home", "labrador" )
parrot  =Parrot("Polly", "Jungle", "squawk")
lion  =Lion("simba", "Savanah", "Pride Rock")

print("===Animal Sound Show ===\n")
for animal in [dog, parrot, lion]:
     animal.display()
     animal.speak()
     print()    