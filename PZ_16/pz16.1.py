"""
Создайте класс "Животное", который содержит информацию о виде и возрасте
животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
"Животное" и содержат информацию о породе
"""
class Animal:
    def __init__(self, species: str, age: int):
        self.species = species
        self.age = age

    def breathe(self):
        print(f"{self.species} дышит.")

    def eat(self):
        print(f"{self.species} питается.")


class Dog(Animal):
    def __init__(self, age: int, breed: str):
        super().__init__(species="Собака", age=age)
        self.breed = breed

    def bark(self):
        print(f"{self.breed} громко гавкает: Гав-гав!")


class Cat(Animal):
    def __init__(self, age: int, breed: str):
        super().__init__(species="Кошка", age=age)
        self.breed = breed

    def purr(self):
        print(f"{self.breed} тихо мурлычет: Мур-мур...")

print("СОБАКА")
dog1 = Dog(age=4, breed="Немецкая овчарка")
dog1.breathe()
dog1.eat()
dog1.bark()


print("КОШКА")
cat1 = Cat(age=2, breed="Сиамская")
cat1.breathe()
cat1.eat()
cat1.purr()
