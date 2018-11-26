import math
import copy


class Town:
    def __init__(self, townId, townEnterFee):
        self.id = townId
        self.adjacent = []
        self.townEnterFee = townEnterFee
        self.partnershipNumber = None

        self.distance = math.inf
        self.previous = None

    def addConnection(self, road):
        self.adjacent.append(road)

    # def __cmp__(self, other):
    #     return self.cmp(self.distance, other.distance)

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

        graph.setTown(self.id, self)
        graph.discountOnPartnershipTownFee(self.partnershipNumber, self.id)


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

    def getTowns(self):
        return self.townDictionary.keys()

    def setTown(self, townId, townNode):
        self.townDictionary[townId] = townNode

    def discountOnPartnershipTownFee(self, partnershipNumber, enteredTownId):
        listOfTowns = self.listOfTownPartnerships[partnershipNumber]

        for town in listOfTowns:
            if town == enteredTownId:
                continue
            else:
                self.getTown(town).townEnterFee = 0


    # def checkIfRoadExists(self, frm, to):
    #     if to in self.townDictionary[frm].getConnections():
    #         return True
    #     else:
    #         return False
