# Parent Pet Class
class Pet:

    noise = "Generic pet noise"

    def __init__(self, name, breed, age, fur_colour, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.fur_colour = fur_colour
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def petting(self):
        print(f"{self.name} is being petted.")

    def speak(self):
        print(self.noise)


# Inherited Dogs
class Dog(Pet):
    noise = "Woof!"


# Instantiating the dog class, to create unique instances i.e. my_dog and my_other_dog
dog1 = Dog("Ruby", "Staffy", 2, "Brown", weight=16)
dog2 = Dog("Happy", "Golden Retriever", 3, "White", weight=30)

# dog2.speak()
# dog2.eat()

# Polymorphic Power Cats
class Cat(Pet):
    noise = "Meow!"


# Instantiating the cat class, to create unique instances i.e. cat1 and cat2
cat1 = Cat("Whiskers", "British Shorthair", 4, "Blue", weight=5)
cat2 = Cat("Sylvester", "Tabby", 5, "Orange", weight=4)

cat1.sleep()
cat2.speak()
cat1.eat()
