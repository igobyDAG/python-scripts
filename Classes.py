class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        return self.passengers.append(name)


flight = Flight(10)
print(flight.capacity)
flight.add_passenger('Daniel')
print(flight.passengers)