from abc import ABC, abstractmethod

class Animal:
    def breath(self):
        pass

    def born(self):
        pass

    @abstractmethod
    def reproduce(self):
        pass


class AsexualAnimal(Animal):
    def reproduce(self):
        print("Reproducing in an Asexual Manner")


class SexualAnimal(Animal):
    def reproduce(self, mate):
        print(f"Reproduce in Sexual Manner whit {mate}")


class OtherAnimal(Animal):
    pass


asexual_animal = AsexualAnimal()
asexual_animal.reproduce()

sexual_animal_a = SexualAnimal()
sexual_animal_b = SexualAnimal()
sexual_animal_a.reproduce(sexual_animal_a)

animal = Animal()
other_animal = OtherAnimal()
