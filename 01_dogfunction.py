# Create a dog object with a function
def dog_factory(name, breed, age):  # name, breed and age are our parameters

    dog = {"name": name, "breed": breed, "age": age}

    return dog


# Calling the create_dog() function to create my_dog. Ruby, Staffy and 2 are our arguments.
dog1 = dog_factory("Ruby", "Staffy", "2")
print(dog1)  # This will output the dog dictionary that we defined within out function

dog2 = dog_factory("Panda", "Great Dane", "6")
