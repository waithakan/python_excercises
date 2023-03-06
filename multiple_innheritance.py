#implementing multiple inheritance



class vehicle:
    def wheels(self):
        print("A car has four wheels")

    def lights(self):
        print("A car has two headlights")

class car (vehicle):#car has inherited attribuites froem vehicle 
    def brakes(self):
        print("A car has two brake pads")

class bus (car):#we are putting this car here to inherit attributes from vehicle without measuring it
    def size(self):
        print("A bus has large capacity")
class train (bus):#this attributes from bus which has inherited froem car which has inherited from vehicle
    def auto(self):
        print("Train does not have auto transmission")
t = train()
t.auto()
t.size()
t.wheels()
t.lights()
t.brakes()