class Animal:
  """
  Base class representing an animal.
  """

  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  """
  Derived class representing a dog inheriting from Animal.
  """

  def __init__(self, name, breed):
    super().__init__(name)  # Call the base class constructor
    self.breed = breed

  def make_sound(self):
    print(f"{self.name} (the dog) barks!")

# Create an Animal instance
animal = Animal("Generic Animal")
animal.make_sound()  # Output: Generic animal sound

# Create a Dog instance
dog = Dog("Buddy", "Labrador")
dog.make_sound()  # Output: Buddy (the dog) barks!
