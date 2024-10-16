from animal import Animal, Dog, Dolphin, Lion, Bird

class AnimalFactory:
  
    def create_animal(animal_type: str) -> Animal:
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'dolphin':
            return Dolphin()
        elif animal_type == 'lion':
            return Lion()
        elif animal_type == 'bird':
            return Bird()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
    

if __name__ == "__main__":
    animal_type = input("Enter the type of animal: ").lower()
    
    try:
        animal = AnimalFactory.create_animal(animal_type)
        print(f"The {animal_type} says {animal.speak()} .")
    except ValueError as e:
        print(str(e))

        