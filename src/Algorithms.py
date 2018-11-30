import heapq
import copy

path = list()
bestPath = None
bestCost = None


def findShortestPathUsingBruteForce(graph, frm, to):  # time here!!!
    bruteForce(graph, frm, to, 0, list())
    print(bestPath, bestCost)


def bruteForce(graph, frm, to, weight, noTownFee):
    global path
    global bestCost
    global bestPath

    frmNode = graph.getTown(frm)
    nextNoTownFee = noTownFee.copy()

    listOfPartnerships = graph.getPartnerships()

    for x in listOfPartnerships:
        if frm in x:
            for y in x:
                if y in noTownFee:
                    continue
                else:
                    nextNoTownFee.append(y)
    path.append(frm)

    if frm == to:
        if bestCost is None or weight < bestCost:
            bestPath = path.copy()
            bestCost = weight

        del path[len(path) - 1]
        return

    neighbours = frmNode.getConnections()

    for x in neighbours:
        if x in path:
            continue
        else:
            nextTown = graph.getTown(x)
            road = frmNode.getRoad(x)
            if x in noTownFee:
                nextWeight = weight + road.getHoursOfDriving() * graph.getCostOfOneHourTrip() + road.getRoadEnterFee()
            else:
                nextWeight = weight + nextTown.getTownEnterFee() + road.getHoursOfDriving() * graph.getCostOfOneHourTrip() + road.getRoadEnterFee()
            bruteForce(graph, x, to, nextWeight, nextNoTownFee)

    del path[len(path) - 1]


# def dijkstra(graph, frm):
#     frmNode = graph.getTown(frm)
#     frmNode.setDistance(0)
#
#     unvisitedQueue = [v for v in graph]
#
#
#     heapq.heapify(unvisitedQueue)
#
#     while len(unvisitedQueue):
#         current = heapq.heappop(unvisitedQueue)
#         current.setVisited()
#
#         for nextNodeId in current.adjacent:
#             nextNode = graph.getTown(nextNodeId)
#             if nextNode.visited:
#                 continue
#
#             road = current.getRoad(nextNodeId)
#             newDist = current.getDistance() + road.getHoursOfDriving() * graph.getCostOfOneHourTrip() + road.getRoadEnterFee() + nextNode.getTownEnterFee()
#
#             if newDist < nextNode.getDistance():
#                 nextNode.setDistance(newDist)
#                 nextNode.setPrevious(current)
#
#         while len(unvisitedQueue):
#             heapq.heappop(unvisitedQueue)
#
#         unvisitedQueue = [v for v in graph if not v.visited]
#         heapq.heapify(unvisitedQueue)

def dijkstrav2(graph, startId, endId):
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
    # # Target Vertex Node
    # node = minTown
    # # Backtrack from the Target Node to the starting node using Predecessors
    # while node is not None:
    #     print('%s' % node.id)
    #     node = node.previous

# def shortest(v, path):
#     if v.previous:
#         path.append(v.previous.getId())
#         shortest(v.previous, path)
#     return

# to = g.getTown(9)
# path = [to.getId()]
# shortest(to, path)
# print(path[::-1], to.getDistance())
