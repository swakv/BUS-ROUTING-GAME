import numpy
from People import People
import random

REJECT_BUSSTOP_COST = 10
CROWDED_COST_MULTIPLIER = 1
class BusStop:

    def __init__(self,name):
        
        # constants
        self.name = name
        self.maxCapacity = 60
        self.discomfortCapacity = 45

        # variables
        self.currentCapacity = 0
        self.people = []
        self.spawnRate = 1

    def __str__(self):
        return self.name + '   ' + str(self.currentCapacity)
        
    def __eq__(self,inp):
        if isinstance(inp,BusStop):
            if inp.name == self.name:
                return True
            else:
                return False

        elif isinstance(inp,str):
            if inp == self.name:
                return True
            else:
                return False

    def setSpawnRate(self,newSpawnRate):
        self.spawnRate = newSpawnRate

    def pickUp(self,bus):

        # store queue of people to board
        boardingPeople = self.people

        # function to make people board when it is crowded
        def crowdedBoard():
            # check queue of people
            # roll to check if they board or not
            while boardingPeople and bus.currentCapacity < bus.maxCapacity:
                # check if they can board by sampling a distribution
                if random.random() < (1-(bus.currentCapacity/bus.maxCapacity)):
                    # remove the person at the front of the queue
                    person = boardingPeople.pop(0)
                    
                    # change the status of the person
                    person.board()
                    # change the required variables in the bus
                    bus.boardBus(self.name,person)
                    # reduce the fullness of the bus stops
                    self.currentCapacity -= 1

        if bus.currentCapacity > bus.discomfortCapacity:
            crowdedBoard()
        else:
            if self.currentCapacity !=len(boardingPeople):
                print(self.currentCapacity,len(boardingPeople))
                raise ValueError
            for x in range(min(self.currentCapacity,bus.discomfortCapacity-bus.currentCapacity)):
                person = boardingPeople.pop(0)
                person.board()
                bus.boardBus(self.name,person)
                self.currentCapacity -= 1

            crowdedBoard()

    def spawn(self):
        # initialise cost
        cost = 0

        # generate the number of people to spawn and make sure that its greater than 0 = n
        numSpawn = numpy.random.normal(loc=self.spawnRate, scale=0.01, size=None)
        numSpawn = max(numSpawn,0)

        # try spawning n people
        for x in range(int(numSpawn)):

            # check if the current number of people in the bus stop is more than the threshold
            # if not keep spawning
            # if so roll to decide to spwan or not
            if self.currentCapacity<self.discomfortCapacity:
                # spwan a person
                person = People()
                self.people.append(person)
                self.currentCapacity+=1
            else:
                # if spwan is unsuccessful, increment cost
                if random.random() < (1-(self.currentCapacity/self.maxCapacity)):
                    # spwan a person
                    person = People()
                    self.people.append(person)
                    self.currentCapacity+=1
                else:
                    # increment cost
                    cost += REJECT_BUSSTOP_COST
        
        return cost

    def step(self):
        cost = 0
        cost += self.crowdedCost()
        cost += self.spawn()
        for person in self.people:
            cost+=person.step()
        return cost
        
    def crowdedCost(self):
        # if the number of people is above a threshold, start adding cost
        if self.currentCapacity > self.discomfortCapacity:
            return CROWDED_COST_MULTIPLIER * self.currentCapacity
        else:
            return 0

if __name__ == "__main__":
    a = BusStop("NS")
    print(a == "NS")
    print("NS" == a)