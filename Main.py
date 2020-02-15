import random
from Route import Route
from Bus import Bus
from BusStop import BusStop

class Main:

    def __init__(self):
        self.busArray = {"red":[],"blue":[]}
        self.busStops = {"red":[],"blue":[]}
        redRouteDetails = Route.getDetails("red")
        blueRouteDetails = Route.getDetails("blue")
        
        for key in list(redRouteDetails.keys()):
            self.busStops['red'].append(BusStop(key))
            
        for key in list(blueRouteDetails.keys()):
            self.busStops['blue'].append(BusStop(key))
        
        self.timeOfDay = "Placeholder"

    def addBus(self,route):
        self.busArray[route].append(Bus(route))

    def removeBus(self,route,bus):
        self.busArray[route].remove(bus)

    def getActiveBuses(self,route):
        return self.busArray[route]
    
    def step(self):
        cost = 0
        for bus in self.busArray['red']:
            cost += bus.step(self)
        
        for bus in self.busArray['blue']:
            cost += bus.step(self)
            
        for busStop in self.busStops['red']:
            cost += busStop.step()
        
        for busStop in self.busStops['blue']:
            cost += busStop.step()
        
        return cost
        
    def getBusStops(self,route):
        return self.busStops[route]

if __name__ == "__main__":
    a = Main()
