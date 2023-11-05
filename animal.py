class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f'{self.name} подает голос')

    def move(self):
        print(f'{self.name} дергает хвостом')

class Dog(Animal):
    def __init__(self, name, breed, legs):
        super().__init__(name, "собака", legs)
        self.breed = breed

    def bark(self):
        print(f'{self.breed} {self.name} лает')

class Bird(Animal):
    def fly(self):
        print(f'{self.species} {self.name} летит')

dog = Dog("Геральт", "доберман", 4)
bird = Bird("Вася", "попугай", 2)

dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()
