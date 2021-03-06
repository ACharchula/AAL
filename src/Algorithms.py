# Antoni Charchuła AAL-2-LS podróż

import heapq
import copy


def dijkstra(graph, startId, endId):
    if len(graph.listOfTownPartnerships) != 0:
        cleanGraph = copy.deepcopy(graph)

    queue = []
    startNode = graph.getTown(startId)
    startNode.distance = 0

    if startNode.partnershipNumber is not None:
        graph.discountOnPartnershipTownFee(startNode.partnershipNumber)
        startNode.visitedPartnerships.append(startNode.partnershipNumber)
        startNode.assignVisitedPartnerships(graph)

    heapq.heappush(queue, startNode)

    while queue:

        current = heapq.heappop(queue)

        if current.id == endId:
            graph.finalTownList.append(current)

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
                    heapq.heapify(queue)
                else:
                    heapq.heappush(queue, nextNode)


def getShortestPath(graph, startNodeId):
    minDistance = 0
    minTown = []

    for town in graph.finalTownList:
        distance = town.distance

        if minDistance > distance or minDistance == 0:
            minDistance = distance
            minTown.clear()
            minTown.append(town)
        elif minDistance == distance:
            minTown.append(town)

    results = []

    for town in minTown:
        path = [town.id]
        node = town

        while node.previous is not None:
            path.append(node.previous.id)
            node = node.previous

        results.append("Shortest trip from town " + str(startNodeId) + " to town - " + str(town.id) + " is: " + str(
            path[::-1]) + " and costs " + str(minDistance))

    return results
