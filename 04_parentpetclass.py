# Parent Pet Class
class Pet:

    noise = "Generic pet noise"

    def __init__(self, name, breed, age, fur_colour):
        self.name = name
        self.breed = breed
        self.age = age
        self.fur_colour = fur_colour

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def petting(self):
        print(f"{self.name} is being petted.")

    def speak(self):
        print(self.noise)


class Dog(Pet):
    noise = "Woof!"


# Inherited Dogs
# Instantiating the dog class, to create unique instances i.e. my_dog and my_other_dog
Dog1 = Dog("Ruby", "", 2, "Brown")
Dog2 = Dog("Happy", "Golden Retriever", 3, "White")

print(Dog2.speak())
Dog1.eat()


# Polymophic Power Cats
class Cat(Pet):
    noise = "Meow!"


# Instantiating the cat class, to create unique instances i.e. Cat1 and Cat2
Cat1 = Cat("Whiskers", "British Shorthair", 4, "Blue")
Cat2 = Cat("Sylvester", "Tabby", 5, "Orange")

Cat1.sleep()
Cat2.speak()
