
class Person:
    counter = 0
    def __init__(self):
        Person.counter += 1
        self.id = Person.counter
        

class Bus:
    def __init__(self, capacity_of_bus, bus_name):
        self.capacity_of_bus = capacity_of_bus
        self.bus_name = bus_name
        self.list_of_passengers = []
    
    def add_passenger(self,person):
        if len(self.list_of_passengers) < self.capacity_of_bus:
            self.list_of_passengers.append(person)
            print(f"Passenger with ID {person.id} added to the bus")
        else:
            print("Capacity of Bus is Full")

    def remove_passenger(self,passenger_id):
        if not self.list_of_passengers:
            print("Bus doesn't have Passengers")
            return
        found = False
        for passenger in self.list_of_passengers:
            if passenger_id == passenger.id:
                self.list_of_passengers.remove(passenger)
                print("Passenger Left the Bus")
                found = True
                break
        if not found:
            print("Passenger not found")











