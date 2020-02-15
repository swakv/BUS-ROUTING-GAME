from Route import Route
import random
from People import People
CROWDED_COST_MULTIPLIER = 1
POLUTION_COST = 10

class Bus:

    # replace start location with starting location in the format: (lastVistedStop,distance)
    def __init__(self, route, totalRounds = 5, startLocation = (" SBS ",1)):

        # graph in the format {"currentBS":{"nextStop":"nextBS","roadWeight":distance}}
        if route == "blue":
            startLocation = (" NIE ",1)

        # constants
        self.route = route #red/blue
        self.startLocation = startLocation
        self.maxCapacity = 60
        self.seats = 30
        self.discomfortCapacity = 45
        self.totalRounds = totalRounds

        # variables        
        self.driverRounds = 0
        self.currentLocation = startLocation
        self.currentCapacity = 0
        self.peopleDisembarkDict = {}

        # initialising peopleDisembarkDict
        routeDetails = Route.getDetails(self.route)
        for key in list(routeDetails.keys()):
            self.peopleDisembarkDict[key] = []

    def __str__(self):
        return str(self.currentCapacity) + '   ' + str(self.currentLocation)
            
    def step(self,main):
        cost = POLUTION_COST
        # store last visited stop and distance from last visited stop
        lastVistedStop = self.currentLocation[0]
        distance = self.currentLocation[1]

        # fetch route deets
        routeDetails = Route.getDetails(self.route)

        # check whether next stop has been reached
        if routeDetails[lastVistedStop]["roadWeight"] == distance+1:

            # store nextStop and update current location
            nextStop = routeDetails[lastVistedStop]["nextStop"]

            self.currentLocation = (nextStop,0)

            # visit the next bus stop
            self.visitBusStop(nextStop,main)

        else:

            # update current location
            self.currentLocation = (lastVistedStop, distance+1)
            
        cost+=self.crowdedCost()

        if self.currentLocation == self.startLocation:
            self.driverRounds+=1

        if self.driverRounds == self.totalRounds:
            main.removeBus(self.route,self)
            return cost

        
        return cost

    def visitBusStop(self,busStop,main):

        # fetch list of busStop objects
        busStops = main.getBusStops(self.route)

        for stop in busStops:
            if stop == busStop:
                # now the required BusStop object is stored in stop
                break
        
        # drop off code
        self.currentCapacity-=len(self.peopleDisembarkDict[busStop])
        self.peopleDisembarkDict[busStop] = []

        # implement pick up code here
        stop.pickUp(self)
    
    def crowdedCost(self):
        # if the number of people is above a threshold, start adding cost
        if self.currentCapacity > self.discomfortCapacity:
            return CROWDED_COST_MULTIPLIER * self.currentCapacity
        else:
            return 0
    
    def boardBus(self,curStop,person):
        disembarkAt = People.chooseDisembarkLocation(curStop,self.route)
        self.peopleDisembarkDict[disembarkAt].append(person)
        self.currentCapacity+=1