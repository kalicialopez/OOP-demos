# Create a dog object with a function
def create_dog(name, breed, age):   # name, breed and age are our parameters

    dog = {
        "name": name,
        "breed": breed,
        "age": age
    }

    return dog


# Calling the create_dog() function to create dog1. Ruby, Staffy and 2 are our arguments.
dog1 = create_dog("Ruby", "Staffy", "2")
print(dog1)     # This will output the dog dictionary that we defined within out function