from animal import Animal, Dog, Dolphin, Lion, Bird

class AnimalDecorator(Animal):
    def __init__(self, animal: Animal):
        self._animal = animal

    def speak(self):
        return self._animal.speak()

class LoudAnimalDecorator(AnimalDecorator):
    def speak(self):
        return f"{self._animal.speak()}!!! (loudly)"

class SoftAnimalDecorator(AnimalDecorator):
    def speak(self):
        return f"{self._animal.speak().lower()}... (softly)"


    
if __name__ == "__main__":
    animal_type = input("Enter the type of animal: ").lower()
    
    
    try:
        if animal_type == 'dog':
            animal = Dog()
        elif animal_type == 'dolphin':
            animal = Dolphin()
        elif animal_type == 'lion':
            animal = Lion()
        elif animal_type == 'bird':
            animal = Bird()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
        
        loud_animal = LoudAnimalDecorator(animal)
        soft_animal = SoftAnimalDecorator(animal)

        print(f"The {animal_type} {loud_animal.speak()}")
        print(f"The {animal_type} {soft_animal.speak()}")

    except ValueError as e:
        print(str(e))
