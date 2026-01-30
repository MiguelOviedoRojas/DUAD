'''class WalkerMixin:
    def walk(self):
        print("I'm walking")


class RunnerMixin:
    def run(self):
        print("I'm running")


class FlyerMixing:
    def fly(self):
        print("I'm flying")


class SuperMan(WalkerMixin, RunnerMixin, FlyerMixing):
    pass


clark_kent = SuperMan()
clark_kent.walk()
clark_kent.run()
clark_kent.fly()'''

class ClassA:
    name = "A"

    def my_method(self):
        print("Hello")


class ClassB:
    name = "B"

    def my_method(self):
        print("Bye")

'''class ClassC(ClassA, ClassB):
    def print_name(self):
        print(f"My name is {self.name}")


my_c = ClassC()
my_c.print_name()
my_c.my_method()'''
print("------------------------------")


class ClassC(ClassB, ClassA):
    def print_name(self):
        print(f"My name is {self.name}")


my_c = ClassC()
my_c.print_name()
my_c.my_method()
