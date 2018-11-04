import heapq

path = list()
bestPath = None
bestCost = None


def findShortestPathUsingBruteForce(graph, frm, to): # time here!!!
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

        print(path)
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


def dijkstra(graph, frm, to):
    frmNode = graph.getTown(frm)
    frmNode.setDistance(0)

    unvisitedQueue = [v for v in graph]
    heapq.heapify(unvisitedQueue)
    while len(unvisitedQueue):
        current = heapq.heappop(unvisitedQueue)
        current.setVisited()

        for nextNodeId in current.adjacent:
            nextNode = graph.getTown(nextNodeId)
            if nextNode.visited:
                continue

            road = current.getRoad(nextNodeId)
            newDist = current.getDistance() + road.getHoursOfDriving() * graph.getCostOfOneHourTrip() + road.getRoadEnterFee() + nextNode.getTownEnterFee()

            if newDist < nextNode.getDistance():
                nextNode.setDistance(newDist)
                nextNode.setPrevious(current)

        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)

        unvisitedQueue = [ v for v in graph if not v.visited]
        heapq.heapify(unvisitedQueue)

def shortest(v, path):
    if v.previous:
        path.append(v.previous.getId())
        shortest(v.previous, path)
    return