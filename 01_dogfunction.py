# Create a dog object with a function called dog_factory
def dog_factory(name, breed, age):  # name, breed and age are our parameters

    dog = {"name": name, "breed": breed, "age": age}

    return dog


# Calling the dog_factory() function to create dog1. "Ruby", "Staffy" and "2" are our arguments.
dog1 = dog_factory("Ruby", "Staffy", "2")
print(dog1)  # This will output the dog dictionary that we defined within our function
# populated with the values we passed through as our arguments.

dog2 = dog_factory("Panda", "Great Dane", "6")
