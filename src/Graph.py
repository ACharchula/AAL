# Antoni Charchuła AAL-2-LS podróż

import math


class Town:
    def __init__(self, townId, townEnterFee):
        self.id = townId
        self.adjacent = []
        self.townEnterFee = townEnterFee
        self.partnershipNumber = None
        self.visitedPartnerships = []
        self.alreadyExpanded = False
        self.distance = math.inf
        self.previous = None

    def addConnection(self, road):
        self.adjacent.append(road)

    def __lt__(self, other):
        return self.distance < other.distance

    def addChangedGraphToAdjacent(self, graph):

        townToSwap = graph.getTown(self.id)

        for road in townToSwap.adjacent:
            self.adjacent.append(road)

            if road.firstTown.id == self.id:
                road.firstTown = self
            else:
                road.secondTown = self

        self.visitedPartnerships.append(self.partnershipNumber)

        # change fee to 0
        for x in self.visitedPartnerships:
            graph.discountOnPartnershipTownFee(x)

        graph.setTown(self.id, self)

        self.assignVisitedPartnerships(graph)

        self.alreadyExpanded = True

    # assign visitedPartnerships to towns in partnerships which were not visited
    def assignVisitedPartnerships(self, graph):

        for partnershipNumber in range(0, len(graph.listOfTownPartnerships)):
            if partnershipNumber in self.visitedPartnerships:
                continue
            else:
                graph.addVisitedPartnerships(partnershipNumber, self.visitedPartnerships)


class Road:
    def __init__(self, roadEnterFee, hoursOfDriving, town1, town2):
        self.roadEnterFee = roadEnterFee
        self.hoursOfDriving = hoursOfDriving
        self.firstTown = town1
        self.secondTown = town2


class GraphOfTowns:
    def __init__(self, costOfOneHourTrip):
        self.listOfTownPartnerships = list()
        self.townDictionary = {}
        self.costOfOneHourTrip = costOfOneHourTrip
        self.finalTownList = []
        self.amountOfRoads = 0

    def __iter__(self):
        return iter(self.townDictionary.values())

    def addNewTownPartnership(self):
        self.listOfTownPartnerships.append(list())

    def addTownToTownPartnership(self, townId, numOfPartnership):
        self.getTown(townId).partnershipNumber = numOfPartnership
        self.listOfTownPartnerships[numOfPartnership].append(townId)

    def addTown(self, townId, townEnterFee):
        newTown = Town(townId, townEnterFee)
        self.townDictionary[townId] = newTown

    def getTown(self, townId):
        if townId in self.townDictionary:
            return self.townDictionary[townId]
        else:
            return None

    def addRoad(self, frm, to, roadEnterFee, hoursOfDriving):

        town1 = self.getTown(frm)
        town2 = self.getTown(to)

        road = Road(roadEnterFee, hoursOfDriving, town1, town2)

        town1.addConnection(road)
        town2.addConnection(road)

        self.amountOfRoads += 1

    def getTowns(self):
        return self.townDictionary.keys()

    def setTown(self, townId, townNode):
        self.townDictionary[townId] = townNode

    def discountOnPartnershipTownFee(self, partnershipNumber):
        listOfTowns = self.listOfTownPartnerships[partnershipNumber]

        for town in listOfTowns:
            self.getTown(town).townEnterFee = 0

    def addVisitedPartnerships(self, partnershipNumber, visitedPartnerships):
        listOfTowns = self.listOfTownPartnerships[partnershipNumber]

        for town in listOfTowns:
            self.getTown(town).visitedPartnerships = visitedPartnerships.copy()

    def checkIfRoadExists(self, frm, to):

        for road in self.townDictionary[frm].adjacent:
            if to == road.firstTown.id or to == road.secondTown.id:
                return True

        return False

    def checkIfTownAlreadyInPartnership(self, townId):
        for partnership in self.listOfTownPartnerships:
            if townId in partnership:
                return True

        return False
