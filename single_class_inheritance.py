# Demonstration of single class ingeritance

class vehicle:
    def wheels(self):
        print("A car has four wheels")

    def lights(self):
        print("A car has two headlights")

class car (vehicle):
    def brakes(self):
        print("A car has two brake pads")

c = car()
c.wheels()
c.lights()
c.brakes()