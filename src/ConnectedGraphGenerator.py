from src.Graph import *
import random
import networkx as nx

# may add more colors if user would like to have more than 7 partnerships (not recommended)
colors = ['blue', 'green', 'orange', 'yellow', 'purple', 'brown', 'magneta']


def checkIfProperData(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
                      minRoadFee, maxRoadLength, minRoadLength, maxTownsInPartnership, minTownsInPartnerships,
                      graphDensity):
    if amountOfTowns <= 0:
        print('Wrong value of amount of towns - please insert value bigger than 0')
        return False
    elif amountOfPartnerships < 0:
        print('Wrong value of amount of partnerships - please insert value bigger or equal 0')
        return False
    elif oneHourCost <= 0:
        print('Wrong value of one hour cost of a trip - please insert value bigger than 0')
        return False
    elif minTownFee <= 0:
        print('Wrong value of minimal town fee - please insert value bigger than 0')
        return False
    elif maxTownFee < minTownFee:
        print('Wrong value of maximal town fee - please insert value bigger or equal minimal town fee')
        return False
    elif minRoadFee <= 0:
        print('Wrong value of minimal road fee - please insert value bigger than 0')
        return False
    elif maxRoadFee < minRoadFee:
        print('Wrong value of maximal road fee - please insert value bigger or equal minimal road fee')
        return False
    elif minRoadLength <= 0:
        print('Wrong value of minimal road length - please insert value bigger than 0')
        return False
    elif maxRoadLength < minRoadLength:
        print('Wrong value of maximal road length - please insert value bigger or equal minimal road length')
        return False
    elif minTownsInPartnerships < 0:
        print('Wrong value of minimal amount of towns in partnership - please insert value bigger than 0')
        return False
    elif amountOfPartnerships > 0 and minTownsInPartnerships < 1:
        print('Wrong value of minimal amount of towns in partnership - please insert value bigger or equal 1')
        return False
    elif maxTownsInPartnership < minTownsInPartnerships:
        print('Wrong value of maximal amount of towns in partnership - please insert value bigger or equal '
              'minimal amount of towns in partnership')
        return False
    elif graphDensity < 2 / amountOfTowns or graphDensity > 1:
        print("Wrong value of graph density - please insert value bigger or egual 2 / amountOfTowns "
              "and smaller or equal 1")
        return False


def prepareDrawing(drawing, color):
    pos = nx.spring_layout(drawing)
    nx.draw(drawing, pos, node_color=color, edge_color='#000000', width=0.25, with_labels=True)

    pos_attr = {}
    for node, coords in pos.items():
        pos_attr[node] = (coords[0], coords[1] + 0.08)

    labels = nx.get_edge_attributes(drawing, 'cost')
    nodesLabels = nx.get_node_attributes(drawing, 'cost')
    nx.draw_networkx_edge_labels(drawing, pos, edge_labels=labels)
    nx.draw_networkx_labels(drawing, pos_attr, labels=nodesLabels)


def prepareColors(amountOfTowns, listOfTownPartnerships):
    color = []

    for i in range(0, amountOfTowns):
        color.append('red')

    partnershipIndex = 0

    for partnership in listOfTownPartnerships:
        for town in partnership:
            color[town] = colors[partnershipIndex]
        partnershipIndex += 1

    return color


def generateConnectedGraph(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
                           minRoadFee, maxRoadLength, minRoadLength, maxTownsInPartnership, minTownsInPartnership,
                           graphDensity):

    drawing = nx.Graph()
    graph = GraphOfTowns(oneHourCost)

    amountOfRoads = int((graphDensity * amountOfTowns * (amountOfTowns - 1)) / 2)
    townFee = random.randint(minTownFee, maxTownFee)

    graph.addTown(0, townFee)
    drawing.add_node(0, cost=townFee)

    for x in range(1, amountOfTowns):
        townFee = random.randint(minTownFee, maxTownFee)
        roadFee = random.randint(minRoadFee, maxRoadFee)
        roadLength = random.randint(minRoadLength, maxRoadLength)

        graph.addTown(x, townFee)
        secondNode = random.randint(0, x - 1)  # random town from previously created towns
        graph.addRoad(x, secondNode, roadFee, roadLength)
        amountOfRoads -= 1

        drawing.add_node(x, cost=townFee)
        drawing.add_edge(x, secondNode, cost=roadFee + roadLength * oneHourCost)

    if amountOfRoads > 0:
        for x in range(0, amountOfRoads):

            added = False

            while not added:
                frm = random.randint(0, amountOfTowns - 1)
                to = random.randint(0, amountOfTowns - 1)

                if frm == to:
                    continue

                if graph.checkIfRoadExists(frm, to):
                    continue
                else:
                    roadFee = random.randint(minRoadFee, maxRoadFee)
                    roadLength = random.randint(minRoadLength, maxRoadLength)

                    graph.addRoad(frm, to, roadFee, roadLength)
                    drawing.add_edge(frm, to, cost=roadFee + roadLength * oneHourCost)
                    added = True

    for x in range(0, amountOfPartnerships):
        graph.addNewTownPartnership()

    partnershipIndex = 0

    if amountOfPartnerships != 0:
        for partnership in graph.listOfTownPartnerships:
            amountOfTownsInPartnership = random.randint(minTownsInPartnership, maxTownsInPartnership)
            for x in range(0, amountOfTownsInPartnership):

                added = False

                while not added:
                    town = random.randint(0, amountOfTowns - 1)

                    if graph.checkIfTownAlreadyInPartnership(town):
                        continue
                    else:
                        partnership.append(town)
                        graph.getTown(town).partnershipNumber = partnershipIndex
                        added = True

            partnershipIndex += 1

    color = prepareColors(amountOfTowns, graph.listOfTownPartnerships)

    prepareDrawing(drawing, color)
    return graph


def generateConnectedGraphWithoutDrawing(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee,
                                         maxRoadFee, minRoadFee, maxRoadLength, minRoadLength, maxTownsInPartnership,
                                         minTownsInPartnership, graphDensity):

    graph = GraphOfTowns(oneHourCost)
    amountOfRoads = int((graphDensity * amountOfTowns * (amountOfTowns - 1)) / 2)
    townFee = random.randint(minTownFee, maxTownFee)
    graph.addTown(0, townFee)

    for x in range(1, amountOfTowns):
        townFee = random.randint(minTownFee, maxTownFee)
        roadFee = random.randint(minRoadFee, maxRoadFee)
        roadLength = random.randint(minRoadLength, maxRoadLength)

        graph.addTown(x, townFee)
        secondNode = random.randint(0, x - 1)  # random town from previously created
        graph.addRoad(x, secondNode, roadFee, roadLength)
        amountOfRoads -= 1

    if amountOfRoads > 0:
        for x in range(0, amountOfRoads):

            added = False

            while not added:
                frm = random.randint(0, amountOfTowns - 1)
                to = random.randint(0, amountOfTowns - 1)

                if frm == to:
                    continue

                if graph.checkIfRoadExists(frm, to):
                    continue
                else:

                    roadFee = random.randint(minRoadFee, maxRoadFee)
                    roadLength = random.randint(minRoadLength, maxRoadLength)

                    graph.addRoad(frm, to, roadFee, roadLength)
                    added = True

    for x in range(0, amountOfPartnerships):
        graph.addNewTownPartnership()

    partnershipIndex = 0

    if amountOfPartnerships != 0:
        for x in graph.listOfTownPartnerships:
            amountOfTownsInPartnership = random.randint(minTownsInPartnership, maxTownsInPartnership)
            for y in range(0, amountOfTownsInPartnership):

                added = False

                while not added:
                    town = random.randint(0, amountOfTowns - 1)

                    if graph.checkIfTownAlreadyInPartnership(town):
                        continue
                    else:
                        x.append(town)
                        graph.getTown(town).partnershipNumber = partnershipIndex
                        added = True
            partnershipIndex += 1

    return graph


def generateGraphFromTxt(listOfData):
    amountOfTowns = listOfData[2]
    amountOfRoads = listOfData[3]
    oneHourTripCost = listOfData[4]
    amountOfPartnerships = listOfData[5]
    amountOfTownsInPartnerships = listOfData[6]

    graph = GraphOfTowns(oneHourTripCost)
    drawing = nx.Graph()

    index = 7

    for x in range(0, amountOfTowns):
        graph.addTown(listOfData[index], listOfData[index + 1])
        drawing.add_node(listOfData[index], cost=listOfData[index + 1])
        index += 2

    for x in range(0, amountOfRoads):
        graph.addRoad(listOfData[index], listOfData[index + 1], listOfData[index + 2], listOfData[index + 3])
        drawing.add_edge(listOfData[index], listOfData[index + 1],
                         cost=listOfData[index + 2] + listOfData[index + 3] * oneHourTripCost)
        index += 4

    for x in range(0, amountOfPartnerships):
        graph.addNewTownPartnership()

    for x in range(0, amountOfTownsInPartnerships):
        graph.addTownToTownPartnership(listOfData[index], listOfData[index + 1])
        index += 2

    townColors = prepareColors(amountOfTowns, graph.listOfTownPartnerships)

    prepareDrawing(drawing, townColors)
    return graph
