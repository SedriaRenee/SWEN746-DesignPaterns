from abc import ABC


class Animal(ABC):
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Dolphin(Animal):
    def speak(self):
        return "whistle"

class Lion(Animal):
    def speak(self):
        return "Roar"
    
class Bird(Animal):
    def speak(self):
        return "Cuh Caw"