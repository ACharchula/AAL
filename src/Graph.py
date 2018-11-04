import math

class Town:
    def __init__(self, townId, townEnterFee):
        self.id = townId
        self.adjacent = {}
        self.townEnterFee = townEnterFee

        self.distance = math.inf
        self.visited = False
        self.previous = None

    def addNeighbour(self, neighbour, road):
        self.adjacent[neighbour] = road

    def getConnections(self):
        return self.adjacent.keys()

    def getId(self):
        return self.id

    def getRoad(self, neighbour):
        return self.adjacent[neighbour]

    def getTownEnterFee(self):
        return self.townEnterFee

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __lt__(self, other):
        return self.getDistance() < other.getDistance()


class Road:
    def __init__(self, roadEnterFee, hoursOfDriving):
        self.roadEnterFee = roadEnterFee
        self.hoursOfDriving = hoursOfDriving

    def getRoadEnterFee(self):
        return self.roadEnterFee

    def getHoursOfDriving(self):
        return self.hoursOfDriving


class GraphOfTowns:
    def __init__(self, costOfOneHourTrip):
        self.listOfTownPartnerships = list()
        self.townDictionary = {}
        self.amountOfTowns = 0
        self.costOfOneHourTrip = costOfOneHourTrip

    def __iter__(self):
        return iter(self.townDictionary.values())

    def getCostOfOneHourTrip(self):
        return self.costOfOneHourTrip

    def getPartnerships(self):
        return self.listOfTownPartnerships

    def addNewTownPartnership(self):
        self.listOfTownPartnerships.append(list())

    def addTownToTownPartnership(self, townId, numOfPartnership):
        self.listOfTownPartnerships[numOfPartnership].append(townId)

    def addTown(self, townId, townEnterFee):
        self.amountOfTowns += 1  # add exception when same id
        newTown = Town(townId, townEnterFee)
        self.townDictionary[townId] = newTown

    def getTown(self, townId):
        if townId in self.townDictionary:
            return self.townDictionary[townId]
        else:
            return None

    def addRoad(self, frm, to, roadEnterFee, hoursOfDriving):
        road = Road(roadEnterFee, hoursOfDriving)

        self.townDictionary[frm].addNeighbour(to, road)
        self.townDictionary[to].addNeighbour(frm, road)

    def getTowns(self):
        return self.townDictionary.keys()

    def checkIfRoadExists(self, frm, to):
        if to in self.townDictionary[frm].getConnections():
            return True
        else:
            return False
