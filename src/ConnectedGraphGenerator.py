from src.Graph import *
import random
import networkx as nx
import matplotlib.pyplot as plt


def generateNumberOfEdges(amountOfVertices):
    maxAmount = amountOfVertices * (amountOfVertices - 1) / 2  # complete graph
    minAmount = amountOfVertices - 1

    return random.randint(minAmount, maxAmount)


def checkIfProperData(amountOfVertices, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
                      minRoadFee, maxRoadLength, minRoadLength, maxTownsInPartnership, minTownsInPartnerships):
    if amountOfVertices <= 0:
        print('Wrong value of vertices - please insert value bigger than 0')
        return False
    elif amountOfPartnerships < 0:
        print('Wrong value of amount of partnerships - please insert value >= 0')
        return False
    elif oneHourCost <= 0:
        print('Wrong value of one hour cost of a trip - pleas insert value bigger than 0')
        return False
    ## TODO


def generateConnectedGraph(amountOfVertices, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
                           minRoadFee, maxRoadLength, minRoadLength, maxTownsInPartnership, minTownsInPartnerships):
    #if not checkIfProperData(amountOfVertices, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
         #                    minRoadFee, maxRoadLength, minRoadLength, maxTownsInPartnership, minTownsInPartnerships):
     #   return

    drawing = nx.Graph()
    graph = GraphOfTowns(oneHourCost)

    amountOfEdges = generateNumberOfEdges(amountOfVertices)

    graph.addTown(0, random.randint(minTownFee, maxTownFee))
    drawing.add_node(0, x=0)

    for x in range(1, amountOfVertices):
        graph.addTown(x, random.randint(minTownFee, maxTownFee))
        secondNode = random.randint(0, x - 1)  # random vertex from previously created
        graph.addRoad(x, secondNode, random.randint(minRoadFee, maxRoadFee),
                      random.randint(minRoadLength, maxRoadLength))
        amountOfEdges -= 1

        drawing.add_node(x, x=x)
        drawing.add_edge(x, secondNode)

    if amountOfEdges != 0:
        for x in range(0, amountOfEdges):

            added = False

            while not added:
                frm = random.randint(0, amountOfVertices - 1)
                to = random.randint(0, amountOfVertices - 1)

                if graph.checkIfRoadExists(frm, to):
                    continue
                else:
                    graph.addRoad(frm, to, random.randint(minRoadFee, maxRoadFee),
                                  random.randint(minRoadLength, maxRoadLength))
                    drawing.add_edge(frm, to)
                    added = True

    for x in range(0, amountOfPartnerships):
        graph.addNewTownPartnership()

    partnershipIndex = 0

    for x in graph.listOfTownPartnerships:
        loops = random.randint(minTownsInPartnerships, maxTownsInPartnership)
        for y in range(0, loops):

            added = False

            while not added:
                town = random.randint(0, amountOfVertices - 1)

                if town in x:
                    continue
                else:
                    x.append(town)
                    graph.getTown(town).partnershipNumber = partnershipIndex
                    added = True
        partnershipIndex += 1

    nx.draw(drawing, with_labels=True)
    plt.show()

    return graph
