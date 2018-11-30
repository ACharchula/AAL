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

    colors = ['blue', 'green', 'orange', 'yellow', 'purple', 'brown', 'magneta']

    drawing = nx.Graph()
    graph = GraphOfTowns(oneHourCost)

    amountOfEdges = generateNumberOfEdges(amountOfVertices)

    townFee = random.randint(minTownFee, maxTownFee)

    graph.addTown(0, townFee)
    drawing.add_node(0, cost = townFee)

    for x in range(1, amountOfVertices):

        townFee=random.randint(minTownFee, maxTownFee)
        roadFee = random.randint(minRoadFee, maxRoadFee)
        roadLength = random.randint(minRoadLength, maxRoadLength)

        graph.addTown(x, townFee)
        secondNode = random.randint(0, x - 1)  # random vertex from previously created
        graph.addRoad(x, secondNode, roadFee, roadLength)
        amountOfEdges -= 1

        drawing.add_node(x, cost = townFee)
        drawing.add_edge(x, secondNode, cost = roadFee + roadLength*oneHourCost)

    if amountOfEdges != 0:
        for x in range(0, amountOfEdges):

            added = False

            while not added:
                frm = random.randint(0, amountOfVertices - 1)
                to = random.randint(0, amountOfVertices - 1)

                if graph.checkIfRoadExists(frm, to):
                    continue
                else:

                    roadFee = random.randint(minRoadFee, maxRoadFee)
                    roadLength = random.randint(minRoadLength, maxRoadLength)

                    graph.addRoad(frm, to, roadFee, roadLength)
                    drawing.add_edge(frm, to, cost=roadFee + roadLength*oneHourCost)
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

    color = []

    for node in drawing:
        color.append('red')

    listOfPartnerships = graph.listOfTownPartnerships

    index = 0

    for partnership in listOfPartnerships:
        for town in partnership:
            color[town] = colors[index]

        index +=1



    pos=nx.spring_layout(drawing)
    nx.draw(drawing,pos, node_color=color, edge_color= '#000000', width=0.25, with_labels=True)

    pos_attr = {}
    for node, coords in pos.items():
        pos_attr[node] = (coords[0], coords[1] + 0.08)

    labels = nx.get_edge_attributes(drawing, 'cost')
    nodesLables = nx.get_node_attributes(drawing, 'cost')
    nx.draw_networkx_edge_labels(drawing,pos, edge_labels=labels)
    nx.draw_networkx_labels(drawing, pos_attr , labels=nodesLables)
    plt.show()
    #plt.savefig("graph.pdf")

    return graph

def generateGraphFromTxt(listOfData):

    colors = ['blue', 'green', 'orange', 'yellow', 'purple', 'brown', 'magneta']

    numberOfTowns = listOfData[2]
    numberOfRoads = listOfData[3]
    oneHourTripCost = listOfData[4]
    numberOfPartnerships = listOfData[5]
    numberOfTownsInPartnerships = listOfData[6]

    graph = GraphOfTowns(oneHourTripCost)
    drawing = nx.Graph()

    index = 7

    for x in range(0,numberOfTowns):
        graph.addTown(listOfData[index], listOfData[index+1])
        drawing.add_node(listOfData[index], cost=listOfData[index+1])
        index += 2

    for x in range(0, numberOfRoads):
        graph.addRoad(listOfData[index], listOfData[index+1], listOfData[index+2], listOfData[index+3])
        drawing.add_edge(listOfData[index], listOfData[index+1], cost=listOfData[index+2] + listOfData[index+3]*oneHourTripCost)
        index += 4

    for x in range(0, numberOfPartnerships):
        graph.addNewTownPartnership()

    townColors = []

    for node in drawing:
        townColors.append('red')

    for x in range(0, numberOfTownsInPartnerships):
        graph.addTownToTownPartnership(listOfData[index], listOfData[index+1])

    listOfPartnerships = graph.listOfTownPartnerships

    index = 0

    for partnership in listOfPartnerships:
        for town in partnership:
            townColors[town] = colors[index]

        index += 1

    pos=nx.spring_layout(drawing)
    nx.draw(drawing,pos, node_color=townColors, edge_color= '#000000', width=0.25, with_labels=True)

    pos_attr = {}
    for node, coords in pos.items():
        pos_attr[node] = (coords[0], coords[1] + 0.08)

    labels = nx.get_edge_attributes(drawing, 'cost')
    nodesLables = nx.get_node_attributes(drawing, 'cost')
    nx.draw_networkx_edge_labels(drawing,pos, edge_labels=labels)
    nx.draw_networkx_labels(drawing, pos_attr , labels=nodesLables)
    plt.show()
    #plt.savefig("graph.pdf")

    return graph











