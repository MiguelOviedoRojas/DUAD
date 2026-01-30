class Vehicle:
    is_on : bool
    wheels : int

    def turn_on(self):
        self.is_on = True
        self.wheels = 4
        print(f"Vehicle is on with {self.wheels} wheels")

    def turn_off(self):
        self.is_on = False
        

class Computer:
    is_on = bool

    def turn_on(self):
        self.operative_system = "windows"
        self.is_on = True
        print(f"Computer is turn on with SO {self.operative_system}")
    
    def turn_off(self):
        self.is_on = False


object_list = [
    Vehicle(),
    Computer(),
    Vehicle(),
    Computer(),
]

for object in object_list:
    object.turn_on()