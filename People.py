from Route import Route
import random

WAITING = 0
BOARDED = 1
COST_PER_TIMESTEP = 1

class People:

    def __init__(self):
        self.timeWaited = 0
        self.status = WAITING
    
    def chooseDisembarkLocation(curStop,route):
        # fetch route details
        routeDetails = Route.getDetails(route)

        # function to check distance in number of bus stops from start
        # we call this distance removal
        def fn(reqd_stop,deets):
            deets[reqd_stop]['removal'] = 0
            x = 0

            # forward pass - add distance in bus stops in direction of the loop
            stop = deets[reqd_stop]['nextStop']
            deets[stop]['prev'] = reqd_stop
            while stop!= reqd_stop:
                x+=1
                deets[stop]['removal'] = x
                nextStop = deets[stop]['nextStop']
                deets[nextStop]['prev'] = stop
                stop = nextStop

            # backward pass - add distance in bus stops opposite direction of the loop
            prev = deets[stop]['prev']
            x= 1
            deets[prev]['removal'] = min(deets[prev]['removal'],x)
            while prev!= reqd_stop:
                prev = deets[prev]['prev']
                x+=1
                deets[prev]['removal'] = min(deets[prev]['removal'],x)
            return deets

        # take total of removals
        routeDetails = fn(curStop,routeDetails)
        total = 0
        for key,value in routeDetails.items():
            if key==curStop:
                continue
            total+=value['removal']

        # generate random value from 0 to total - 1
        randVal = random.randint(0,total-1)
        
        # pick the cumulative region in which the random value falls and return that region
        total = 0
        for key,value in routeDetails.items():
            if key==curStop:
                continue
            total+=value['removal']
            if randVal<total:
                break
        
        return key


    def board(self):
        self.status = BOARDED

    def step(self):
        if self.status == WAITING:
            self.timeWaited += 1
            return COST_PER_TIMESTEP
        else:
            return 0