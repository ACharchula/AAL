import heapq
import copy

# path = list()
# bestPath = None
# bestCost = None


def dijkstrav2(graph, startId, endId):
    copyAmount = 0

    cleanGraph = copy.deepcopy(graph)

    queue = []
    startNode = graph.getTown(startId)
    startNode.distance = 0

##powtorka kodu! podobne w addchngedgraphtoAdjacent

    if startNode.partnershipNumber is not None:
        graph.discountOnPartnershipTownFee(startNode.partnershipNumber)
        amountOfPartnerships = len(graph.listOfTownPartnerships)
        index = 0
        while index < amountOfPartnerships:
            if index == startNode.partnershipNumber:
                index += 1
                continue
            else:
                l = list()
                l.append(startNode.partnershipNumber)
                graph.addVisitedPartnerships(index, l)
                index += 1

    heapq.heappush(queue, startNode)

    while queue:

        #for x in queue:
        #    print(' == ', x.id)

        current = heapq.heappop(queue)

        if current.id == endId:
            graph.finalTownList.append(current)

        #print(current.id)

        if current.partnershipNumber is not None and current.townEnterFee != 0 and current.alreadyExpanded is not True:

            copied = copy.deepcopy(cleanGraph)
            copyAmount += 1
            current.addChangedGraphToAdjacent(copied)

        for road in current.adjacent:

            if road.secondTown.id != current.id:
                nextNode = road.secondTown
            else:
                nextNode = road.firstTown

            newDistance = current.distance + road.hoursOfDriving * graph.costOfOneHourTrip + road.roadEnterFee \
                          + nextNode.townEnterFee

            if newDistance < nextNode.distance:
                nextNode.previous = current
                nextNode.distance = newDistance

                if nextNode in queue:
                    queue.remove(nextNode)

                heapq.heappush(queue, nextNode)


def getShortestPath(graph, startNodeId):
    minDistance = 0  ##pokaz wszystkie sciezki nei tylko jedna -- do zmienienia
    minTown = None

    for town in graph.finalTownList:
        distance = town.distance

        if minDistance > distance or minDistance == 0:
            minDistance = distance
            minTown = town

    path = [minTown.id]

    node = minTown

    while node.previous is not None:
        path.append(node.previous.id)
        node = node.previous

    result = "Shortest trip from town " + str(startNodeId) + " to town - " + str(minTown.id) + " is: " + str(path[::-1]) + " and costs " + str(minDistance)

    return result

