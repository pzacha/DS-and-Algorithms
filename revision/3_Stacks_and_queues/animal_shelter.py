import unittest


class Animal:
    order = 1

    def __init__(self, species, name):
        if species != "dog" and species != "cat":
            raise Exception("Wrong spiece")
        self.species = species
        self.name = name
        self.order = Animal.order
        Animal.order += 1

    def __str__(self):
        return self.name


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, a):
        if a.species == "dog":
            self.dogs.append(a)
        else:
            self.cats.append(a)

    def get_oldest(self):
        if len(self.cats) == 0:
            return "dog"
        elif len(self.dogs) == 0:
            return "cat"

        if self.cats[0].order > self.dogs[0].order:
            return "dog"
        else:
            return "cat"

    def dequeueAny(self):
        self.is_empty()
        oldest = self.get_oldest()
        if oldest == "dog":
            return (self.dogs.pop(0)).name
        else:
            return (self.cats.pop(0)).name

    def dequeueCat(self):
        if len(self.cats) == 0:
            raise Exception("No cats")
        return self.cats.pop(0).name

    def dequeueDog(self):
        if len(self.dogs) == 0:
            raise Exception("No dogs")
        return self.dogs.pop(0).name

    def is_empty(self):
        if len(self.cats) == 0 and len(self.dogs) == 0:
            raise Exception("Queue is empty")


class Test(unittest.TestCase):
    test_data = AnimalShelter()
    test_data.enqueue(Animal("dog", "Dog1"))
    test_data.enqueue(Animal("dog", "Dog2"))
    test_data.enqueue(Animal("cat", "Cat1"))
    test_data.enqueue(Animal("dog", "Dog3"))
    test_data.enqueue(Animal("cat", "Cat2"))
    o1 = test_data.dequeueAny()
    o2 = test_data.dequeueCat()

    def test_animal_shelter(self):
        self.assertEqual(self.o1, "Dog1")
        self.assertEqual(self.o2, "Cat1")


if __name__ == "__main__":
    unittest.main()
