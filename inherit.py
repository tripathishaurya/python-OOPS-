# class animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# class dog(animal):
#         def speak(self):
#             print(f"{self.name} barks")


# Animal=animal("Generic Animal")
# Animal.speak()

# Dog=dog("buddy")
# Dog.speak()
class Animal:
    def __init__(self):
        self.name="buddy"

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed
    def speak(self):
        super().speak()
        print(f"{self.name} barks . it is a {self.breed}")

dog=Dog("desi")
dog.speak()